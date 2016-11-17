from finance.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', accounts_page, name="accounts_page"),
    url(r'^account/(?P<pk>[0-9]+)/$', account_details_page, name="account_details_page"),
]