from django.conf.urls import url
import telepot
from channels.channel import Group
import json
from chats.botwrapper import BotWrapper

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


run_already = [False]

def startup():
    if run_already[0]:
        return

    run_already[0] = True

    # print('start telegram bot')

    hr_assistant = BotWrapper('assistant', '<API_TOKEN>')

startup()
