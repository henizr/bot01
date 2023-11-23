import telebot


API_TOKEN = '6427191316:AAEUI2mYgRhWkzogKn7lo4vUMCOUwu-gnto'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hi! I`m a bot.")

@bot.message_handler(commands=["hello"])
def greeting(message):
    bot.reply_to(message, "Hello, my dear friend! I`m glad to see you!")


@bot.message_handler(content_types=['text'])
def answer(message):

    text = message.text

    bot.reply_to(message,f"Ты отправил(а) сообщение: '{text}'")

bot.polling(none_stop=True, interval=0)
