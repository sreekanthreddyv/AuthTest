# !python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth.views import login, logout
from log.forms import LoginForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^login/$', login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}),
]
