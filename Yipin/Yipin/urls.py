"""Yipin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

#1
from . import view, testdb, search, search2

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search_form$', search.search_form),
    url(r'^search$', search.search),
    
    url(r'^search-post$', search2.search_post),
    url(r'^display-meta', view.display_meta),
    url(r'search-form/$', view.search_form),
    url(r'^search2/$', view.search2),
    url(r'^test-form/$', view.test_formView),

]

urlpatterns += [
    url(r'^TestApp/', include('TestApp.urls', namespace='TestApp)),
]
urlpatterns += [
    url(r'^User/', include('User.urls', namespace='User')),
]
