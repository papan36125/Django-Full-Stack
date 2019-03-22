from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.view_users, name='view_users'),
]
