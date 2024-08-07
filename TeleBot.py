import telebot
from telebot import types
from config import *
from Texts import *

centres = ["Центр 1","Центр 2", "Центр 2"]
users_centre = []

bot = telebot.TeleBot(token=TELEBOT_API_KEY)

keyboard_centres_markup = types.InlineKeyboardMarkup()
for centre in centres:
    btn = types.InlineKeyboardButton(centre, callback_data=centre)
    keyboard_centres_markup.row(btn)

@bot.message_handler(commands=["start", "menu"])
def user_start_bot(message):
    if message == "start":
        bot.send_message(message.chat.id, FIRST_MESSAGE_UA, reply_markup=keyboard_centres_markup)
    else:
        pass

@bot.callback_query_handler(func=lambda callback: True)
def callback_handler(callback):
    if callback.data in centres:
        bot.send_message(callback.message.chat.id, "Дякую, ваш вибір збережено. \nТепер введіть, будь ласка, наступні дані: Призвище Ім'я")
        bot.register_next_step_handler(callback.data, checkIfCustomerInBase)

def checkIfCustomerInBase(message):
    pass

bot.infinity_polling()