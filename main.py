# PIL imports
from PIL import Image, ImageOps, ImageChops
import pytesseract
# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# Misc imports
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


botToken = config.get('BOT', 'botAPI')
botChatID = config.get('BOT', 'botChat')

def screen(URL):
    # Setup webdriver

    DRIVER = 'resources/chromedriver'
    chromeOptions = Options()
    # chromeOptions.headless = True
    driver = webdriver.Chrome(DRIVER, options=chromeOptions)
    driver.set_window_size(('1920'),('1080'))
    driver.get(URL)

    # Get button for popup and click
    button = driver.find_element_by_class_name("close")
    button.click()
    html = driver.find_element_by_tag_name('html')

    # Page down and sleep
    html.send_keys(Keys.PAGE_DOWN)
    sleep(1)

    # Take Screen
    screenshot = driver.save_screenshot('images/image.png')
    driver.quit()

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    with open(file,'w') as outFile:
        outFile.write(pytesseract.image_to_string(Image.open(filename)))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
        outFile.close
    # return text

def parse():
    keywords = ['Sold Out','Available today','to subscribe to back in stock e-mails','Add to Cart']
    with open(file,'r') as openFile:
        lines = openFile.readlines()
        for l in lines:
            for word in keywords:
                if word in l:
                    if word == keywords[0] or word == keywords[2]:
                        return('Out of stock')
                        # return("{}".format(l.strip()))
                    elif word == keywords[1] or word == keywords[3]:
                        return('Available ' +URL)
                    else:
                        return('Keywords not found, please check page '+URL)
                else:
                    return ('Maybe in stock. '+URL)

def botMessage(message):
    print(message)
    botMessage = message
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&parse_mode=Markdown&text=' + botMessage

def greyscale(image):
    img = Image.open(image).convert('L')
    greyscale = ImageOps.invert(img)
    img.save('images/greyscale.png')



if __name__ == '__main__':
    # URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
    URL = 'https://store.ui.com/collections/unifi-protect-cameras/products/unifi-protect-g4-pro-camera'
    # URL = 'https://store.ui.com/collections/unifi-protect-cameras/products/unifi-protect-g3-instant-camera'
    file = 'test.txt'
    screen(URL)
    greyscale('images/image.png')
    ocr_core('images/greyscale.png')
    msg = parse()
    botMessage(msg)
