from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup')
]

# from . import views
# from django.conf.urls import url, include
# from django.urls import path
 
# urlpatterns = [
#     url(r'^$', views.index, name='home'),
#     path('signup/', views.signup, name='signup'), # newly added
# ]