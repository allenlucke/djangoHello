from django.urls import path
from django.conf.urls import url
from todo import views
from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home"),
    url(r'^api/todos$', views.todo_list),
]