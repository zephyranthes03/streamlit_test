import telegram
import telebot
import os

bot = telebot.TeleBot(os.getenv("TELEGRAM_API"))

@bot.message_handler(commands=['info'])
def send_welcome(message):
    name = bot.get_me()
    print(name)
    bot.reply_to(message, "Welcome")

bot.polling()
