from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcements/', views.announcements, name='announcements'),
    path('announcement/<int:pk>/', views.announcement_detail, name='announcement_detail'),
    path('announcement/create/', views.create_announcement, name='create_announcement'),
]