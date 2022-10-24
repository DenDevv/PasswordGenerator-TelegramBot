from telebot import types


home_page = types.ReplyKeyboardMarkup(resize_keyboard=True)
home_page.row(types.KeyboardButton(text='🔑 Generate password'),
                types.KeyboardButton(text='🔎 Password verification'))