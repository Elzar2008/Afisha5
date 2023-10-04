from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_list_create_api_view),
    path('categories/<int:id>/', views.categories_item_update_delete_api_view),
    path('products/', views.product_list_create_api_view),
    path('products/<int:id>/', views.product_item_update_delete_api_view),
    path('reviews/', views.review_list_create_api_view),
    path('reviews/<int:id>/', views.review_item_update_delete_api_view),
    path('products/reviews/', views.product_reviews_list_api_view),
    path('tags/', views.tag_list_create_api_view),
]

