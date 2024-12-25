import cv2
from ultralytics import YOLO

class ImageAnalyzer:
  def __init__(self):
    self.model = YOLO("trained-model.pt")
                
  def has_mallet(self, frame: cv2.Mat, confidence = 0.5) -> bool:
    # TODO: Check for mallets
    results = self.model(frame)
    for result in results:
      result.show()
      
      json = result.summary()
      print(json)
      if len(json) == 0: return False

      if json[0]['name'] == "mallet" and json[0]['confidence'] > confidence:
        return True
      
    return False