from config import token
import telebot
from random import choice
import random

API_TOKEN = token
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    

@bot.message_handler(commands=['random'])
def random_handler(message):
    bot.reply_to(message, random.randint(0,150))


@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, "Привет я Ботик")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
    


bot.infinity_polling()
