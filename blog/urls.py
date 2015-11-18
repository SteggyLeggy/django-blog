import djangae
from django.conf.urls import url, include
from django.contrib import staticfiles
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    url(r'^gauth/', include(djangae.contrib.gauth.urls)),
    url(r'^new/$', views.save_new_blog, name='save_new_blog'),
    url(r'^save/$', views.create_blog, name='create_blog'),
    url(r'^category/(?P<slug>[a-zA-Z0-9\-]+)/$', views.category, name='category'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)/$', views.blog_detail, name='detail'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)/edit/$', views.edit_blog, name='edit_blog'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)/update/$', views.update_existing_blog, name='update_existing_blog'),
]