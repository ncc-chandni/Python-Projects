import cv2
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np 
from pylab import rcParams
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Update this path if Tesseract is installed elsewhere


rcParams['figure.figsize'] = 8, 16

file_name = '/Users/umakantmanore/Desktop/amu/Dev_Enviroment2023/test_env/Python-Projects/Image_to_text/text.jpeg'

img = cv2.imread(file_name)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

text_out = pytesseract.image_to_string(img)

print(text_out)

