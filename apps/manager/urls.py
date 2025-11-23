from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path("", views.manager_home, name="home"),
    path("create/", views.manager_create, name="create"),
    path("edit/<int:id>/", views.manager_edit, name="edit"),
    path("delete/<int:id>/", views.manager_delete, name="delete"),
]
