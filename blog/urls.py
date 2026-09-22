from django.urls import path
from . import views

urlpatterns = [
    path('', views.TimerPageView.as_view(), name='home'),
    path('timer/', views.TimerStreamView.as_view(), name='timer'),
]
