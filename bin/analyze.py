import cv2

from lib.analyzer import ImageAnalyzer

def main():
  analyzer = ImageAnalyzer()

  no_mallet = cv2.imread("no_mallet.jpg")
  assert analyzer.has_mallet(no_mallet) == False, "Found mallet when there is no mallet"

  yes_mallet = cv2.imread("yes_Mallet.jpg")
  assert analyzer.has_mallet(yes_mallet) == True, "Could not detect mallet"


main()
