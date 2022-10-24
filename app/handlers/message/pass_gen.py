import secrets
from config import bot
from app.models.keyboards import home_page
from string import ascii_letters, digits, punctuation, ascii_uppercase, ascii_lowercase


def password_generation(message):
    chat_id = message.from_user.id
    password = ""
    create_password = ""
    args = ['-l', '-u', '-d', '-s']
    default_password_settings = ascii_letters + digits + punctuation

    try:
        password_len = message.text.split()[1]

        if not password_len.isdigit():
            bot.send_message(chat_id, "The length must be in numbers!")
            return

        if all(arg in args for arg in message.text.split()):
            
            for _ in range(int(password_len)):
                password += secrets.choice(default_password_settings)
            
            if not any(i in digits for i in password):
                password = password.replace(secrets.choice(password[secrets.randbelow(len(password))]), secrets.choice(digits))

            bot.send_message(chat_id, f'🔑 <i>Generated password:</i> \n\n<code>{password}</code>', parse_mode='html')
            return

        if '-l' in message.text.split():
            create_password += ascii_lowercase
        
        if '-u' in message.text.split():
            create_password += ascii_uppercase
        
        if '-d' in message.text.split():
            create_password += digits

        if '-s' in message.text.split():
            create_password += punctuation
        
        for _ in range(int(password_len)):
            password += secrets.choice(create_password)
        
        if not any(i in digits for i in password):
            password = password.replace(secrets.choice(password[secrets.randbelow(len(password))]), secrets.choice(digits))

        bot.send_message(chat_id, f'🔑 <i>Generated password:</i> \n\n<code>{password}</code>', parse_mode='html', reply_markup=home_page)

    except IndexError:
        bot.send_message(chat_id, "You did not specify a length!")