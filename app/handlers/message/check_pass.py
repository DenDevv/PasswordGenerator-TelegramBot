from config import bot
from string import punctuation
from app.models.keyboards import home_page


def check_pass(message):
    chat_id = message.chat.id

    return_val=True
    result_msg = 'āļø <i>Your password is not secure!</i> ā ļø\nš <u>Here are the reasons:</u>\n'

    if len(message.text) < 8:
        result_msg += '\nā ļø <b>Password must be at least 8 characters long.</b>'
        return_val=False
    
    if not any([char.isdigit() for char in message.text]):
        result_msg += '\nā ļø <b>The password must contain at least one digit.</b>'
        return_val=False

    if not any([char.isupper() for char in message.text]):
        result_msg += '\nā ļø <b>The password must contain at least one uppercase letter.</b>'
        return_val=False

    if not any([char.islower() for char in message.text]):
        result_msg += '\nā ļø <b>The password must contain at least one lowercase letter.</b>'
        return_val=False

    if not any([char in punctuation for char in message.text]):
        result_msg += f'\nā ļø <b>The password must contain at least one of the following chars:</b> \'~ ! @ # $ % & * _ - = + , . ? \/ " | ;\''
        return_val=False

    if not return_val:
        bot.send_message(chat_id, result_msg, parse_mode='html', reply_markup=home_page)
        return

    bot.send_message(chat_id, 
                    ('š <i>Characteristics of the password:</i>\n\n',
                    f'š <b>Length:</b> {len(message.text)}\n\n',
                    f'š <b>Number of digits</b>: {len([int(i) for i in message.text if i.isdigit()])}\n\n',
                    f'š <b>Number of uppercase letters:</b> {len([str(i) for i in message.text if i.isupper()])}\n\n',
                    f'š <b>Number of lowercase letters:</b> {len([str(i) for i in message.text if i.islower()])}\n\n',
                    f'š <b>Number of special chars:</b> {len([i for i in message.text if i in punctuation])}\n\n',
                    '<b>Success!</b> š„³\nš” <b>Your password is secure and you can use it!</b> ā'),
                    parse_mode='html', reply_markup=home_page)