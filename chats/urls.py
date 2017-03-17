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
    # appleTalker = BotWrapper('apple', '251927694:AAE7JxhJP8tjvzNxreIKQXgdRA3Cc0cnVEQ')

    hr_assistant = BotWrapper('assistant', '357768893:AAHCQM6l50c-5739D40viWL2b7-ERk7ffOA')
    # cheeseTalker = BotWrapper('cheese', '306868573:AAGZ0Jx1G32mJOicDzqbgwvLRdrdySh3vzs')

    # chickenTalker = BotWrapper('chicken', '342362127:AAEXUguhhuAPO2I82D2HilSvp2X6tSj-XAY')

startup()