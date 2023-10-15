from django.urls import path

from peach.views import ListItemView

urlpatterns = [
    path("items",ListItemView.as_view(),name="list_items"),
]