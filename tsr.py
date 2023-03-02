import pytesseract as pyte
from PIL import ImageGrab
import pyautogui as pyat
import time

pyte.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

a = pyte.image_to_string('1010.PNG', lang='jpn_vert', config='--psm 5 --oem 1')

print(a)