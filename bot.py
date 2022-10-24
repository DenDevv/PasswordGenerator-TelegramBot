from config import bot
from app.handlers.message.chat import chat
from app.models import commands


bot.register_message_handler(commands.start, commands=['start'])


@bot.message_handler(content_types=['text'])
def messages(message):
    chat(message)


bot.polling(none_stop=False, interval=0)