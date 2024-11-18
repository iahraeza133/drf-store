from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import Category, ProductList, CommentViewSet, CartViewSet, CartItemViewSet
from .views import CustomerViewSet
# Create a main router for categories, products, and carts
router = DefaultRouter()
router.register(r'categories', Category, basename='category')
router.register(r'products', ProductList, basename='product')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'customers', CustomerViewSet)

# Nested router for comments under products
product_router = NestedDefaultRouter(router, r'products', lookup='product')
product_router.register(r'comments', CommentViewSet, basename='product-comments')

# Nested router for cart items under carts
cart_router = NestedDefaultRouter(router, r'carts', lookup='cart')
cart_router.register(r'items', CartItemViewSet, basename='cartitems')

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Main URLs (categories, products, carts)
    path('', include(product_router.urls)),  # Nested URLs for product comments
    path('', include(cart_router.urls)),  # Nested URLs for cart items
]



# urlpatterns = [
#     # path('products/', views.product_list, name='product_list'),            # URL for product list
#     # path('products/<int:pk>/', views.product_detail, name='product_detail'),
#     # path('categories/', views.Category_list, name='category_list'),  # List all categories
#     # path('categories/<int:pk>/', views.Category_detail, name='category_detail'), 
#     # 
#     # # Detail view for a single category# URL for product detail by ID
    
    
#     path('categories/', CategoryList.as_view(), name='category-list'),  # دریافت لیست دسته‌بندی‌ها
#     path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),  # دریافت، به‌روزرسانی، حذف دسته‌بندی

#     # Product URLs
#     path('products/', ProductList.as_view(), name='product-list'),  # دریافت لیست محصولات
#     path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),  # دریافت، به‌روزرسانی، حذف محصول 
    
    
# ]
