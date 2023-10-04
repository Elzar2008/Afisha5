from rest_framework import serializers
from .models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


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
        fields = 'id name'.split()


class CategoryValidateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=128)


class ProductValidateSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField()
    price = serializers.IntegerField(min_value=0)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exists')
        return category_id


class ReviweCreateValidateSerializers(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()
    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exists')
        return product_id


class ReviweUpdateValidateSerializers(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=1, max_value=5)


class TagValidateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=0, max_length=100)
    products = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_products(self, products):
        product_id = list(Product.objects.values_list("id", flat=True))
        errors = {}
        for index, value in enumerate(products):
            if not value in product_id:
                errors[index] = [f'Product does not exists']
        if errors:
            raise ValidationError(errors)
        return products