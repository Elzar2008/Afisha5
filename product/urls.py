from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/<int:id>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view()),
    path('products/reviews/', views.ProductReviewsListAPIView.as_view()),
    path('products/reviews/<int:id>/', views.ProductRetrieveAPIView.as_view()),
    path('tags/', views.TagListCreateAPIView.as_view()),
    path('tags/<int:id>/', views.TagRetrieveUpdateDestroyAPIView.as_view()),
]

