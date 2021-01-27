# PIL imports
from PIL import Image, ImageOps, ImageChops
import pytesseract

def ocr_core(file,imagename):
    """
    This function will handle the core OCR processing of images.
    """
    with open(file,'w') as outFile:
        outFile.write(pytesseract.image_to_string(Image.open(imagename)))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
        outFile.close
    # return text

def greyscale(image):
    img = Image.open(image).convert('L')
    greyscale = ImageOps.invert(img)
    img.save('images/greyscale.png')
