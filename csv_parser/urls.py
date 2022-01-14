from django.conf.urls import url
from csv_parser import views

urlpatterns = [
    url(r'^api/test$', views.test),
    url(r'^api/csvtest1$', views.file_test_1),
    url(r'^api/csvtest2$', views.file_test_2),
]