import telepot
from channels.channel import Group
from users.models import Person, City
import json
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import uuid
from chats.botlogic import Logic


class BotWrapper:

    def __init__(self, name, TOKEN):
        self.name = name
        self.token = TOKEN
        self.bot = telepot.Bot(self.token)
        self.bot.message_loop(self.handle)

    def handle(self, msg):
        content_type, chat_type, chat_id= telepot.glance(msg)
        #  print(content_type, chat_type, chat_id)

        from_username = msg['from']['username']
        from_id  = msg['from']['id']
        l = Logic()
        user = self.try_get_user(from_id, chat_id)
        l.state_machine(self.bot, user, msg)
        return

    # try find if user already exist
    def try_get_user(self, from_id, chat_id):
        try:
            user = Person.objects.get(telegram_id=from_id)
            print('already exist')
        except:
            l = Logic()
            user = Person(telegram_id = from_id, chat_id=chat_id)
            l.set_state(user, 'init')
            l.set_inner_state(user, '0')
            user.save()

        print(user)
        return user
