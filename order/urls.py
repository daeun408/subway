from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
app_name = 'order'

urlpatterns = [
    path('', views.order, name='order'),
    path('history/', views.history, name='history')
]