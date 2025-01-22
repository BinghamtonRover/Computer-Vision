print("Initializing...")

import cv2
import os

from lib.analyzer import ImageAnalyzer
analyzer = ImageAnalyzer()


def test(): 
  for file in os.listdir("test_images"): 

    filename, _ = file.split(".")
    if not filename: continue 
    """ print(f"file is: {file}")
    print(f"!filename is:{filename}")     """             # chair_yes.jpg --> chair_yes, jpg
    background, has_mallet = filename.split("_")  # chair_yes --> chair, yes
    has_mallet = has_mallet == "yes"              # yes --> True
    frame = cv2.imread(f"test_images/{file}")
    result = analyzer.has_mallet(frame)
    if result == has_mallet: 
      print(f"{background} image passed -- {result}")
    else: 
      print(f"{background} image failed: Analyzer detected {result} instead of {has_mallet}")


def main():
  print("Loading model...")
  
  no_mallet = cv2.imread("no_mallet.jpg")
  yes_mallet = cv2.imread("yes_Mallet.jpg")

  print("Analyzing no_mallet... ", end = "")
  found_mallet = analyzer.has_mallet(no_mallet)
  if found_mallet:
    print("Failed\nFound mallet when there is no mallet")
    return
  print("Success!")

  print("Analyzing yes_mallet... ", end = "")
  found_mallet = analyzer.has_mallet(yes_mallet)
  if not found_mallet:
    print("Failed\nCould not detect mallet")
    return
  print("Success!")

if __name__ == "__main__":
  main()
  test()

