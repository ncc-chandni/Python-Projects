import pytesseract
from PIL import Image
import cv2 

'''
Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.
'''

'''
OCR Engine modes: (see https://github.com/tesseract-ocr/tesseract/wiki#linux)
  0    Legacy engine only.
  1    Neural nets LSTM engine only.
  2    Legacy + LSTM engines.
  3    Default, based on what is available.
'''


myconfig = r"--psm 6 --oem 3"

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Update this to the correct path

# Your existing code
text = pytesseract.image_to_string(Image.open("/Users/umakantmanore/Desktop/amu/Dev_Enviroment2023/test_env/Python-Projects/Image_to_text/hsd_mri.jpeg"), config='--psm 6')
print(text)



myconfig = r"--psm 11 --oem 3"

img = cv2.imread("/Users/umakantmanore/Desktop/amu/Dev_Enviroment2023/test_env/Python-Projects/Image_to_text/hsd_mri.jpeg")
height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
print(boxes)

for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)


cv2.imshow("img", img)
cv2.waitKey(0)

