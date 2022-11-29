from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'calendar', views.CalendarView.as_view(), name='calendar'), # here

]
