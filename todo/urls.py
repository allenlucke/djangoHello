from django.urls import path
from django.conf.urls import url
from todo import views
from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home"),
    url(r'^api/todos$', views.todo_list),
    url(r'^api/todos/(?P<pk>[0-9]+)$', views.todo_detail),
    url(r'^api/todos/completed$', views.todo_list_completed)
]