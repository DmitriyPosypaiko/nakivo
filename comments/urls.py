from django.urls import path
from .views import add_comment_to_post

urlpatterns = [
    path('product/<int:pk>/add_comment', add_comment_to_post, name='add_comment'),

]