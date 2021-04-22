from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiListMail, name='api-mail-list'),
    path('email-list/', views.mailList, name='todo-list'),
    path('email-detail/<str:pk>', views.mailDetail, name='mail-detail'),
    path('email-create/', views.mailCreate, name='mail-create'),
    path('email-updates/<str:pk>', views.mailUpdate, name='mail-updates'),
    path('email-delete/<str:pk>', views.mailDelete, name='mail-delete'),
    # path('email-send/<str:pk>', views.mailSend, name='mail-send'),
]
