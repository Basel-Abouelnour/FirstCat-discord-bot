import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message =='hello cat':
        return 'MEOW!'

    if message == 'roll':
        return str(random.randint(1,6))

    if message == 'owner':
        return 'MESHMESH-sama is my owner'

    if p_message == '!help':
        return '`meow,meow meow meow' \
               ' MEOW!!`'

    return "NO MEOW!!"