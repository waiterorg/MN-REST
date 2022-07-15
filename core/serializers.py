from rest_framework import serializers

from .models import Category, Mobile


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category table
    """

    class Meta:
        model = Category
        fields = [
            "title",
            "slug",
        ]


class MobileSerializer(serializers.ModelSerializer):
    """
    Serializer for Mobile table
    """

    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Mobile
        fields = [
            "title",
            "price",
            "category",
            "description",
            "image",
            "production_date",
        ]
