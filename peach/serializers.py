from rest_framework import serializers

from peach.models import Item


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #fields="__all__"
        exclude=("description",)

