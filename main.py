import os
import cv2
import csv
import tempfile
import pytesseract
from tqdm import tqdm
from PIL import Image, ImageOps
from pdf2image import convert_from_path

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


# this function extract data "No. urut keluarga terbesar"
# to an image (png) from page 2 of SLS documents and save it
# to processing folder.
def getTotalNumberImage(path):
  fname = os.path.splitext(os.path.basename(path))[0]

  images = convert_from_path(path)

  output_filename = os.path.join(os.getcwd(), "processing", '{}.png'.format(fname))

  # this is magic number to crop"No. urut keluarga terbesar",
  # left, top, bottom, rigth pixel position.
  images[1].crop((1545, 90, 1625, 130)).resize((720, 360)).save(output_filename, "png")


# extracted images will be read by tesseract
# to get the number in the image.
def getTextFromImage(path):
  img = cv2.imread(path)   

  text = pytesseract.image_to_string(img)

  return text


# run script to all SLS document
def run():
  pdfPath = os.path.join(os.getcwd(), "data")
  imagePath = os.path.join(os.getcwd(), "processing")

  print('Extract data from SLS...')

  for file in tqdm(os.listdir(pdfPath)):
    if file.endswith(".pdf"):
      getTotalNumberImage(os.path.join(pdfPath, file))

  print('Compiling result ...')

  for file in tqdm(os.listdir(imagePath)):
    if file.endswith(".png"):
      text = getTextFromImage(os.path.join(imagePath, file))

      with open('result.csv', mode='a') as result:
        csvResult = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csvResult.writerow([
          os.path.splitext(os.path.basename(file))[0], 
          text.strip() 
        ])

if __name__ == '__main__':
  run()