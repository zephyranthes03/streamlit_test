import telegram
import telebot

bot = telebot.TeleBot("7439567925:AAGjEEXzSFO_DwDlfaQ6uZ8jGKy25sx8rKI")

@bot.message_handler(commands=['info'])
def send_welcome(message):
    name = bot.get_me()
    print(name)
    bot.reply_to(message, "Welcome")

bot.polling()
