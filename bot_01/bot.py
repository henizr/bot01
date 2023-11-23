import telebot


API_TOKEN = '6427191316:AAEUI2mYgRhWkzogKn7lo4vUMCOUwu-gnto'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler()
def start(message):
    bot.reply_to(message, "Hello!")
    # print("Hi")


bot.polling(none_stop=True, interval=0)
