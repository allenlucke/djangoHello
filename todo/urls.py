from django.urls import path
from django.conf.urls import url
from todo import views
from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home"),
    url(r'^api/todos$', views.todo_list),
    url(r'^api/todos/(?P<pk>[0-9]+)$', views.todo_detail),
    url(r'^api/todos/completed$', views.todo_list_completed),
    url(r'^api/todos/is_completed/(?P<bool>[0-1]+)$', views.todo_list_is_completed),
    url(r'^api/todos/switch/(?P<pk>[0-9]+)$', views.todo_switch_is_completed),

    url(r'^api/users', views.users_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^api/users/is_active/(?P<bool>[0-1]+)$', views.users_list_is_active),

    url(r'^api/todos/user/(?P<user_id>[0-9]+)$', views.todo_list_by_user),
    url(r'^api/todos/user/(?P<user_id>[0-9]+)/(?P<is_complete>[0-1]+)$', views.todo_list_by_user),
]