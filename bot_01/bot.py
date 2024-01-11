import telebot


API_TOKEN = '6427191316:AAEUI2mYgRhWkzogKn7lo4vUMCOUwu-gnto'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 
                     "Привет! Давай сыграем в игру — ты загадаешь число от 1 до 100, а я отгадаю его."
                     " Чтобы начать игру, используй команду /start_game") 
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 
                     "Привет! Вот список доступных команд:\n/start - начало работы\n/start_game "
                     "- начинаем игру\n/help - список доступных команд") 

bot.polling(none_stop=True, interval=0)
