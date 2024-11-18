from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer,CommentSerializer
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from .models import Category,Comment
from .serializers import CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from .models import Category
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter 

from rest_framework import status

















# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':
#         # Handle GET request: retrieve and return a list of products
#         queryset = Product.objects.select_related('category')  # Use select_related to optimize database queries
#         serializer = ProductSerializer(queryset, many=True, context={'request': request})  # Pass 'request' in context for hyperlinked fields
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # Handle POST request: create a new product
#         serializer = ProductSerializer(data=request.data, context={'request': request})  # Pass 'request' in context for hyperlinked fields
        
#         if serializer.is_valid():  # Check if the data is valid
#             serializer.save()  # Save the new product
#             return Response(serializer.data, status=201)  # Return the created product with a 201 status code
#         else:
#             return Response(serializer.errors, status=400) 


# class ProductList(APIView):
    
#     def get(self, request):
#         queryset = Product.objects.select_related('category')  
#         serializer = ProductSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)  # رفع مشکل تورفتگی
    
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():  # بررسی اعتبار داده‌ها
#             serializer.save()  # ذخیره محصول جدید
#             return Response(serializer.data, status=HTTP_201_CREATED)  # بازگشت محصول ایجاد شده با کد ۲۰۱
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  #











# @api_view(['GET', 'PUT', 'PATCH'])
# def product_detail(request, pk=None):
#     try:
#         product = Product.objects.get(pk=pk)  # Get the Product instance by pk
#     except Product.DoesNotExist:
#         return Response({"error": "Product not found"}, status=404)

#     # Handle PUT request (full update)
#     if request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()  # Save the updated product
#             return Response(serializer.data)  # Return the updated product data
#         return Response(serializer.errors, status=400)

#     # Handle PATCH request (partial update)
#     elif request.method == 'PATCH':
#         serializer = ProductSerializer(product, data=request.data, partial=True, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()  # Save the partially updated product
#             return Response(serializer.data)  # Return the updated product data
#         return Response(serializer.errors, status=400)

#     # Handle GET request (retrieve single product data)
#     elif request.method == 'GET':
#         serializer = ProductSerializer(product, context={'request': request})
#         return Response(serializer.data)
# class ProductDetail(APIView):
    
#     def get(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)  # دریافت محصول با کلید اصلی (pk)
#         except Product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=HTTP_404_NOT_FOUND)  # مدیریت خطای محصول یافت‌نشده

#         serializer = ProductSerializer(product, context={'request': request})
#         return Response(serializer.data)  # بازگشت داده‌های سریالایز شده
    
#     def put(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)  # دریافت محصول با کلید اصلی
#         except Product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=HTTP_404_NOT_FOUND)

#         serializer = ProductSerializer(product, data=request.data, partial=True, context={'request': request})
#         if serializer.is_valid():  # بررسی اعتبار داده‌های ورودی
#             serializer.save()  # ذخیره محصول به‌روزرسانی‌شده
#             return Response(serializer.data)  # بازگشت محصول به‌روزرسانی‌شده
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  # بازگشت خطا در صورت نامعتبر بودن داده‌ها

#     def delete(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)  # دریافت محصول با کلید اصلی
#         except Product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=HTTP_404_NOT_FOUND)

#         product.delete()  # حذف محصول
#         return Response(status=HTTP_204_NO_CONTENT)# بازگشت کد 204 با خالی کردن محتوا#


# from rest_framework import generics
# from .models import Product
# from .serializers import ProductSerializer
# from rest_framework import generics
# from .models import Product
# from .serializers import ProductSerializer

# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.select_related('category')  # Use select_related to optimize queries involving 'category'
#     serializer_class = ProductSerializer  



# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.select_related('category').all()  # Queryset to retrieve product
#     serializer_class = ProductSerializer  # Specify the serializer class
    
    
# def delete(self, request, pk):
#     try:
#         # Try to get the product with the given pk
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         # If the product does not exist, return a 404 error
#         return Response({"error": "Product not found"}, status=HTTP_404_NOT_FOUND)

#     # If the product exists, delete it
#     product.delete()

#     # Return a 204 No Content response after deletion
#     return Response(status=HTTP_204_NO_CONTENT)

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter 
class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category')  # Use select_related to optimize queries involving 'category'
    serializer_class = ProductSerializer
    filterset_class = ProductFilter  # Apply the 


    
def destroy(self, request, pk=None):
        try:
            # Retrieve the product by primary key (pk)
            product = self.get_object()  # get_object() is automatically provided by ModelViewSet
        except Product.DoesNotExist:
            # Return a 404 error if the product does not exist
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # If the product exists, delete it
        product.delete()

        # Return a 204 No Content response after deletion
        return Response(status=status.HTTP_204_NO_CONTENT)








# @api_view(['GET'])
# def Category_list(request):
#     queryset = Category.objects.all()
#     serializer = CategorySerializer(queryset, many=True)  # Specify many=True for multiple objects
#     return Response(serializer.data)

#  class CategoryList(APIView):
#     def get(self, request):
#          queryset = Category.objects.annotate(products_count=Count('products')).all()  # اضافه کردن تعداد محصولات مرتبط
#          serializer = CategorySerializer(queryset, many=True, context={'request': request})
#          return Response(serializer.data, status=HTTP_200_OK)
    
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()  # ذخیره داده‌های معتبر
#             return Response(serializer.data, status=HTTP_201_CREATED)  # بازگشت پاسخ موفقیت‌آمیز
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  # بازگشت خطای داده‌های نامعتبر




# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.annotate(products_count=Count('products')) 
#     serializer_class = CategorySerializer  # T











# class CategoryDetail(APIView):
#     def get(self, request, pk):
#         try:
#             # محاسبه تعداد محصولات مرتبط برای یک دسته‌بندی خاص
#             category = Category.objects.annotate(products_count=Count('products')).get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({"error": "Category not found"}, status=HTTP_404_NOT_FOUND)
        
#         serializer = CategorySerializer(category, context={'request': request})
#         # اضافه کردن تعداد محصولات به داده‌های بازگشتی
#         serialized_data = serializer.data
#         serialized_data['products_count'] = category.products_count
        
#         return Response(serialized_data, status=HTTP_200_OK)
    
#     def put(self, request, pk):
#         try:
#             category = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({"error": "Category not found"}, status=HTTP_404_NOT_FOUND)
        
#         serializer = CategorySerializer(category, data=request.data, partial=True, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         try:
#             category = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({"error": "Category not found"}, status=HTTP_404_NOT_FOUND)
        
#         category.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
    
    
from .permissions import IsAdminOrReadOnly
class Category(viewsets.ModelViewSet):
    # queryset = Category.objects.prefetch_related('products').all()
    queryset = Category.objects.annotate(products_count=Count('products'))
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def destroy(self, request, pk=None):
        try:
            # Try to get the category with the given pk
            category = self.get_object()  # Using the built-in get_object() from ModelViewSet
        except Category.DoesNotExist:
            # If the category does not exist, return a 404 error
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        # If the category exists, delete it
        category.delete()

        # Return a 204 No Content response after deletion
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    # با��گشت کد 204 با خالی کردن محتوا
    
    # مدیریت خطای دسته‌بندی یافت نشده
# @api_view(['GET', 'POST'])  # می‌توانید GET و POST را در یک دکوریتور قرار دهید
# def Category_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             # یافتن دسته‌بندی با pk مشخص
#             queryset = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             # در صورت عدم وجود دسته‌بندی
#             return Response({"error": "Category not found"}, status=404)
        
#         # سریالایزر برای دسته‌بندی
#         serializer = CategorySerializer(queryset)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # ایجاد دسته‌بندی جدید
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  # ذخیره دسته‌بندی جدید
#             return Response(serializer.data, status=201)  # پاسخ موفقیت‌آمیز با وضعیت 201
#         else:
#             return Response(serializer.errors, status=400)

class CommentViewSet(viewsets.ModelViewSet):
    
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        product_pk=self.kwargs['product_pk']
        return Comment.objects.filter(product_id=product_pk).all()
    
from . models import Cart
from . serializers import CartSerializer


from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet
from .models import Cart,CartItem
from .serializers import CartSerializer,CartItemSerializer
from rest_framework.mixins import DestroyModelMixin
class CartViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):  # Remove extra parentheses here
    queryset = Cart.objects.prefetch_related('items__product').all()  # Define the queryset for the ViewSet
    serializer_class = CartSerializer  # Specify the serializer class
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()  # Get all CartItem objects
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_pk = self.kwargs['cart_pk']  # Get the cart ID from the URL
        return CartItem.objects.select_related('product').filter(cart_id=cart_pk)
    
    
    
    
from rest_framework.decorators import action
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Customer
from .serializers import CustomerSerializer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]  # By default, requires the user to be authenticated

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user_id = request.user.id
        try:
            customer = Customer.objects.get(user_id=user_id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def update_profile(self, request):
        user_id = request.user.id
        try:
            customer = Customer.objects.get(user_id=user_id)
            # Optionally, update fields of customer using data from request.data
            serializer = CustomerSerializer(customer, data=request.data, partial=True)  # partial=True allows for partial updates
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
