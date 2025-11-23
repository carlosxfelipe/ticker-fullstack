from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [
    path("", views.wallet_home, name="home"),
    path("create/", views.wallet_create, name="create"),
    path("edit/<int:id>/", views.wallet_edit, name="edit"),
    path("delete/<int:id>/", views.wallet_delete, name="delete"),
]
