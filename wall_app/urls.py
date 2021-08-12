from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #GET request to display all objects' info starting at root
    path('wall', views.wall), #GET request to display all objects' info starting at a different root
    path('wall/new_wall', views.add_wall), #GET request to display form to create an object
    path('wall/create_wall', views.create_wall), #POST request to create an object
    path('wall/<int:wall_id>', views.view_wall), #GET request to display a specific object's info
    path('wall/<int:wall_id>/edit', views.edit_wall), #GET request to display form to update a specific object
    path('wall/<int:wall_id>/update', views.update_wall), #POST request to update a specific object
    path('wall/<int:wall_id>/destroy', views.delete_wall), #POST request to delete a specific object
]