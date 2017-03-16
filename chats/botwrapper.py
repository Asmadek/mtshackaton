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
                'bot': self.namaname
            })})


    # try find if user already exist
    def try_get_user(self):
        print('test')

    # get info by vk
    def try_set_info_by_vk(self, user):
        print('test')

    # get information by direct questions
    def set_info(self, user):
        print('test')

    # get category (student, oldest) by direct questions
    def get_category(self, user):
        print('test')

    def set_university(self, user):
        print('test')

    def set_areas(self, user):
        print('test')

    def testing(self, user, area):
        print('test')

    def send_decline(self, user):
        print('test')

    def set_marked_vacancies(self, user):
        print('test')
        
    def set_phone_number(self, user):
        print('test')

