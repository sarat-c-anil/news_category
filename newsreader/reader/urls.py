# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('news/<str:category>/', views.display_news, name='display_news'),
    # Other URL patterns
]