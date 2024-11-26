import cv2

from lib.analyzer import ImageAnalyzer

def main():
  analyzer = ImageAnalyzer()

  no_mallet = cv2.imread("no_mallet.jpg")
  if analyzer.has_mallet(no_mallet):
    print("Error: Found mallet when there is no mallet")
    return

  yes_mallet = cv2.imread("yes_Mallet.jpg")
  if not analyzer.has_mallet(yes_mallet):
    print("Error: Could not detect mallet")
    return


main()
