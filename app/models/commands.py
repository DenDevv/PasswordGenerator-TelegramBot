from config import bot
from app.models.keyboards import home_page


def start(message):
    bot.send_message(message.chat.id, '🔐 Password generator.\n\nSelect a function from the menu below 👇', reply_markup=home_page)