from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import (CategorySerializer, ProductSerializer, ProductReviewsListSerializer, ReviewSerializer,
                          CategoryValidateSerializers, ProductValidateSerializers, ReviweCreateValidateSerializers,
                          ReviweUpdateValidateSerializers, TagSerializer, TagValidateSerializers)
from .models import Category, Product, Review, Tag


# Category
@api_view(['GET', 'POST'])
def categories_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(instance=categories, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategoryValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        name = serializer.validated_data.get('name')
        category = Category.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED, data=CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def categories_item_update_delete_api_view(request, id):
    try:
        categories = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = CategorySerializer(instance=categories, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CategoryValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        categories.name = serializer.validated_data.get('name')
        categories.save()
        return Response(data=CategorySerializer(categories).data,
                        status=status.HTTP_202_ACCEPTED)


# Product
@api_view(['GET', 'POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(instance=products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        products = Product.objects.create(
            title=title, description=description, price=price, category_id=category_id
        )
        return Response(status=status.HTTP_201_CREATED, data=ProductSerializer(products).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_item_update_delete_api_view(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductSerializer(instance=products, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ProductValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        products.title = serializer.validated_data.get('title')
        products.description = serializer.validated_data.get('description')
        products.price = serializer.validated_data.get('price')
        products.category_id = serializer.validated_data.get('category_id')
        products.save()
        return Response(data=ProductSerializer(products).data,
                        status=status.HTTP_202_ACCEPTED)


# Review
@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviweCreateValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        product_id = serializer.validated_data.get('product_id')
        review = Review.objects.create(
            text=text, stars=stars, product_id=product_id
        )
        return Response(status=status.HTTP_201_CREATED, data=ReviewSerializer(review).data)


@api_view(['GET'])
def product_reviews_list_api_view(request):
    products = Product.objects.all()
    data = ProductReviewsListSerializer(instance=products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def review_item_update_delete_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(instance=reviews, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviweUpdateValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        reviews.text = request.data.get('text')
        reviews.stars = request.data.get('stars')
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data,
                        status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
def tag_list_create_api_view(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        data = TagSerializer(instance=tags, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TagValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        name = serializer.validated_data.get('name')
        products = serializer.validated_data.get('products')
        tags = Tag.objects.create(name=name)
        tags.products.set(products)
        tags.save()
        return Response(status=status.HTTP_201_CREATED, data=TagSerializer(tags).data)




