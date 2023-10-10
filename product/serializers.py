from rest_framework import serializers
from .models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars product'.split()


class ProductReviewsListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title description price rating reviews'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price category'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count products'.split()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'id name products'.split()