import json
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels.channel import Group
import telepot

def http_request_consumer(message):


    response = HttpResponse('Well %s' % message.content['path'])


    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)



def ws_connect(message):
    Group('chat').add(message.reply_channel)

def ws_message(message):
    msg = json.loads(message.content['text'])
    print(msg)

    if 'to' in msg:
        print('hasattr')
        TOKEN = ''

        if msg['bot'] == 'apple':
            TOKEN = '251927694:AAE7JxhJP8tjvzNxreIKQXgdRA3Cc0cnVEQ'
        elif msg['bot'] == 'chicken':
            TOKEN = '342362127:AAEXUguhhuAPO2I82D2HilSvp2X6tSj-XAY'
        elif msg['bot'] == 'cheese':
            TOKEN = '306868573:AAGZ0Jx1G32mJOicDzqbgwvLRdrdySh3vzs'
        elif msg['bot'] == 'assistant':
            TOKEN = '357131666:AAHcYHgT57ibjUPP2AlB0M_z2STtDLI-O7M'
            
        bot = telepot.Bot(TOKEN)
        bot.sendMessage(msg['to'], msg['message'])
        
    Group('chat').send({'text': json.dumps({
        'message': message.content['text'],
        'sender': message.reply_channel.name,
        'from': 'dashboard'
    })})

def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)