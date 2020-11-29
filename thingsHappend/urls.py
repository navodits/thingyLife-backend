from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts_list),
    path("<str:_id>", views.posts_detail),    
]