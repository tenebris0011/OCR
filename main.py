# Misc imports
from seleniumMethods import screen
from parsing import parse
from parsing import botMessage
from ocr import greyscale
from ocr import ocr_core

if __name__ == '__main__':
    # URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
    # URL = 'https://store.ui.com/collections/unifi-protect-cameras/products/unifi-protect-g4-pro-camera'
    URL = 'https://store.ui.com/collections/unifi-protect-cameras/products/unifi-protect-g3-instant-camera'
    file = 'OCR.txt'
    screen(URL)
    greyscale('images/image.png')
    ocr_core(file,'images/greyscale.png')
    msg = parse(file,URL)
    botMessage(msg)
