
fro:m django.conf.urls import include, url
from django.contrib import admin
#
from .views import *
urlpatterns = [
    url(r'^Yiyipin/Book/$', Book, name='Book'),
    url(r'^time/plus/(\d{1,2}/$)', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^salesStatistics/list/$', salesStatisticsListView, name = 'salesStatistics-list' )
    url(r'^errors_form/$',contact, name='contact'),
]
