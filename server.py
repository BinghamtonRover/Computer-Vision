from lib.analyzer import ImageAnalyzer
import asyncio
from lib.network import *
from lib.network.generated import Connect, Device, DriveCommand, VideoData

class AnalyzerServer:
	def __init__(self, socket: UdpSocket):
		self.analyzer = ImageAnalyzer()
		self.socket = socket
		try:
			self.socket = socket
            
			self.socket.listen("Frame", VideoData, self.handle_frame)
			
		except Exception as e:
			print(f"init error: {str(e)}")
			raise

	def handle_frame(self, frame):
		frame = self.analyzer.annotateImage(frame)
		self.socket.send_message(frame)

	async def run(self):
		try:
			await self.socket.serve_forever()
            
		except Exception as e:
			self.logger.error(f"error: {str(e)}")
		
		finally:
			await self.cleanup()


	def cleanup(self):
		self.socket.close();
  
async def main():
	port = 8001
	socket = await UdpSocket.create(port=port, device=Device.SUBSYSTEMS)
	server = AnalyzerServer(socket=socket)
	await server.run()


if __name__ == "__main__":
    asyncio.run(main())