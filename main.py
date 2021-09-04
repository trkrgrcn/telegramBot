from telegram.ext import Updater, CommandHandler
import random
import json



PRICE = '/p <symbol>'

def loadFile(filename):
    with open(filename) as file:
        data = json.load(file)
        return data

def start(update, context):
    update.message.reply_text('/p ETH')





def main():
    api = loadFile('apikey.json')
    updater = Updater(api['Apis'][0]["TelegramBotApi"], use_context=True)
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("sor", sor))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
