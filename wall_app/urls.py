from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall), #GET request to display all objects' info starting at a different root
    path('create_message', views.create_message), #POST request to create an object,
    path('create_comment', views.create_comment), #POST request to create an object
    # path('/<int:_id>/destroy', views.delete_), #POST request to delete a specific object
]