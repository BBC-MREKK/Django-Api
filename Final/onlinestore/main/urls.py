from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('show_categories/', cats, name='cats'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='show_post')
]