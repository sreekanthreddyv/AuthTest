#!python
# log/urls.py
from django.conf.urls import url
from .views import home

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', home, name='home'),
]
