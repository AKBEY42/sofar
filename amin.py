import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Merhaba! ŞOFAR Lojistik Bot çalışıyor.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Aldım: {message.text}")

bot.infinity_polling()
