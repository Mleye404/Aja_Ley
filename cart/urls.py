from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("ajouter/<slug:slug>/", views.add_to_cart, name="add_to_cart"),
    path("mensurations/<slug:slug>/", views.measurements, name="measurements"),
    path("article/<int:item_id>/quantite/", views.update_quantity, name="update_quantity"),
    path("article/<int:item_id>/supprimer/", views.remove_item, name="remove_item"),
    path("article/<int:item_id>/mensurations/", views.edit_measurements, name="edit_measurements"),
]
