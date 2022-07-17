from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from datetime import date, time
import random


TOKEN = '5552068886:AAH-FFz09ckXPrVF2o9aks0igeFo84Qy5wY'


numbers = []
for num in range(-2, 101):
    numbers.append(num)


# This function replies with 'Hello <user.first_name>'
def hashari(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'جنابالي {random.choice(numbers)} درصد حشري اي')

def kooni(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'جنابالي {random.choice(numbers)} درصد کوني اي')

def mame(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{random.choice(numbers)}')

def logbat(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'جنابالي {random.choice(numbers)} درصد لگبتي')

kalbas = ['داشت', 'نداشت']
def raftam_baghali(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'رفتم بقالي کالباس {random.choice(kalbas)}')

kosht = ['پشه کشت','عرضه نداشت يه پشه بکشه']
tatal = ['ناراحت شد','تخمش بود']
def pashe(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'پيشرو {random.choice(kosht)} تتلو {random.choice(tatal)}')


# Insert your token here
updater = Updater('5552068886:AAH-FFz09ckXPrVF2o9aks0igeFo84Qy5wY')


# Make the hello command run the hello function
updater.dispatcher.add_handler(CommandHandler('hashari', hashari))
updater.dispatcher.add_handler(CommandHandler('kooni', kooni))
updater.dispatcher.add_handler(CommandHandler('mame', mame))
updater.dispatcher.add_handler(CommandHandler('logbat', logbat))
updater.dispatcher.add_handler(CommandHandler('raftam_baghali', raftam_baghali))
updater.dispatcher.add_handler(CommandHandler('pashe', pashe))


# Connect to Telegram and wait for messages
updater.start_polling()


# Keep the program running until interrupted
updater.idle()
