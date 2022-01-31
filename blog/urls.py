from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('gallery', views.show_gallery)
]