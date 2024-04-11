import telebot

bot = telebot.TeleBot('6802602446:AAHfa9fv2M5N3bv8xB1Z-qj-ufYhPUNNK6Y')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Вітаю! Я ваш бот.")
    
bot.polling()