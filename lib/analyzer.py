import cv2
from ultralytics import YOLO

class ImageAnalyzer:
  def __init__(self):
    self.model = YOLO("trained-model.pt")
                
  def has_mallet(self, frame: cv2.Mat) -> bool:
    # TODO: Check for mallets
    results = self.model(frame)
    print("CALLING HAS MALLET")
    for result in results:
      result.show()
    return False