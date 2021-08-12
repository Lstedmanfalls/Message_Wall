from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall), #GET request to display all objects' info starting at a different root
    path('create_message', views.create_message), #POST request to create an object
    # path('/<int:_id>', views.view_), #GET request to display a specific object's info
    # path('/<int:_id>/edit', views.edit_), #GET request to display form to update a specific object
    # path('/<int:_id>/update', views.update_), #POST request to update a specific object
    # path('/<int:_id>/destroy', views.delete_), #POST request to delete a specific object
]