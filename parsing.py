# Parsing Imports
import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')


botToken = config.get('BOT', 'botAPI')
botChatID = config.get('BOT', 'botChat')


def parse(file,URL):
    keywords = ['Sold Out','Available today','to subscribe to back in stock e-mails','Add to Cart']
    with open(file,'r') as openFile:
        lines = openFile.readlines()
        for l in lines:
            for word in keywords:
                if word in l:
                    # print(word)
                    if word == keywords[0] or word == keywords[2]:
                        return('Out of stock\n' +URL)
                        # return("{}".format(l.strip()))
                    elif word == keywords[1] or word == keywords[3]:
                        return('Available\n' +URL)
                    else:
                        return('Keywords not found, please check page\n'+URL)
                # else:
                #     return ('Maybe in stock.\n'+URL)

def botMessage(message):
    print(message)
    botMessage = message
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&parse_mode=Markdown&text=' + botMessage
    requests.get(sendText)