from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^show$', views.show_candidate, name='show'),
    url(r'^list$', views.list_candidate, name='list'),
]