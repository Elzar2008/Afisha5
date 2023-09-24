from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer, ProductReviewsListSerializer, ReviewSerializer
from .models import Category, Product, Review


# Category
@api_view(['GET', 'POST'])
def categories_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(instance=categories, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
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
        categories.name = request.data.get('name')
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
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
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
        products.title = request.data.get('title')
        products.description = request.data.get('description')
        products.price = request.data.get('price')
        products.category_id = request.data.get('category_id')
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
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
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
        reviews.text = request.data.get('text')
        reviews.stars = request.data.get('stars')
        reviews.product_id = request.data.get('product_id')
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data,
                        status=status.HTTP_202_ACCEPTED)



