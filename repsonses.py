import random

def get_response(message: str) -> str:
  p_message = message.lower()
  """
  INPUT MUST BE LOWERCASE!  
  """
  #Greetings
  if p_message == 'hi':
    return '`اهلا يحبيب اخوك`'
  if p_message == 'bye':
    return '`مع السلامة ياخويا`'

  if p_message == 'hello cat':
    return '`MEOW!`'

  if p_message == 'love you':
    return '`FirstCat Love U2` :anatomical_heart:'  #Anatomical Heart Emotion

  if message == 'roll':
    return str(random.randint(1, 99))

  if message == 'owner':  #FirstCat.py line: 57, 58
    return 'Basel#4470'

  if message == 'مياو':
    return 'meow'

  # if p_message == 'help':
  #   return '```TRY :hi , bye\t  ' \
  #           '\n\t hello cat\t \n\t love you\t'\
  #           '\n\t roll\t  \n\t owner\t \n\t cat pic'\
  #           '\n\t and more coming ! ```:wink:'
  
  #Commented Because It Replies To All Messages Except Commands 
  # return "`Someting went wrong` :crying_cat_face:"        #Crying Cat Emotion
