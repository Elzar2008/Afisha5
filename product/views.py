from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .models import Category, Product, Review


@api_view(['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(instance=categories, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def categories_item_api_view(request, id):
    try:
        categories = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    data = CategorySerializer(instance=categories, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(instance=products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_item_api_view(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ProductSerializer(instance=products, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_item_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(instance=reviews, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)
