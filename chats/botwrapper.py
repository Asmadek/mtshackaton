import telepot
from channels.channel import Group
import json

class BotWrapper:

    def __init__(self, name, TOKEN):
        self.name = name
        self.token = TOKEN
        self.bot = telepot.Bot(self.token)
        self.bot.message_loop(self.handle)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        #  print(content_type, chat_type, chat_id)

        if content_type == 'text':
            #  print(msg['text'])
            Group('chat').send({
                'text': json.dumps({
                'message': msg['text'],
                'sender': chat_id,
                'from': 'telegram',
                'bot': self.name
            })})
