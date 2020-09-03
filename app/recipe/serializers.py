from rest_framework import serializers
from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """ Leírás: Serializer for tag objects """

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )


class IngredientSerializer(serializers.ModelSerializer):
    """ Leírás: Serializer for ingredient objects """

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id', )