from config import bot
from app.handlers.message.pass_gen import password_generation
from app.handlers.message.check_pass import check_pass


def chat(message):
    chat_id = message.from_user.id

    try:
        if message.chat.type == 'private':
            if message.text == 'š Generate password':
                bot.send_message(chat_id, 
                                ('š <b>Password generation</b>\n\nāļø <b>For generation, copy this:</b> ',
                                '<code>/gen 25 -l -u -d -s</code>\n\n<i>-l -- lowercase letters\n-u -- uppercase letters\n',
                                '-d -- digits\n-s -- special chars\n25 -- length (can be arbitrary)</i>\n\n<b>',
                                'You can not write all parameters, but choose as you wish, but if you just write ',
                                '<i>/gen <u>length</u></i>, password will be created by default settings!</b>'), parse_mode='html')

            if message.text == 'š Password verification':
                bot.send_message(chat_id, 'š <i>Password verification.\n\nš Write me the password you want to check...</i>', parse_mode='html')

                if message.from_user.id:
                    bot.register_next_step_handler(message, check_pass)
            
            if message.text.split()[0] == '/gen':
                password_generation(message)
    except:
        pass