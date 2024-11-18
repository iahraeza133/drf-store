from rest_framework import serializers
from .models import Product, Category,Comment,Cart, Customer
from decimal import Decimal
from django.utils.text import slugify

# class CategorySerializer(serializers.Serializer):
#     num_of_products = serializers.SerializerMethodField()
#     # id = serializers.IntegerField()  # استفاده از IntegerField به جای Column
#     title = serializers.CharField(max_length=255)
#     top_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
class CategorySerializer(serializers.ModelSerializer):
    num_of_products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'title', 'top_product','num_of_products']
    
    def get_num_of_products(self, category):
     return category.products_count 
    
    
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20, source='name')
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory = serializers.IntegerField()
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category = CategorySerializer()
    category=serializers.HyperlinkedRelatedField(queryset=Category.objects.all(),view_name='category-detail')
    DOLLAR_TO_RIAL = Decimal('50000')  # تبدیل به Decimal
    price_in_rial = serializers.SerializerMethodField()
    price_with_tax = serializers.SerializerMethodField(method_name='price_tax')
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'inventory', 'category']
    def get_price_in_rial(self, product):
        # از Decimal برای ضرب استفاده می‌کنیم تا دقت را حفظ کنیم
        return round(product.unit_price * (1 + Decimal('0.05')) * self.DOLLAR_TO_RIAL, 2)

    def price_tax(self, product):
        return round(product.unit_price * (1 + Decimal('0.05')) * self.DOLLAR_TO_RIAL, 2)
    
    
    #cusTOM  validation
    def validate(self, data):
        if len(data['title']) < 6:  # Change 'name' to 'title'
            raise serializers.ValidationError('Title should be at least 6 characters long.')
        return data

     #
     # 
     # این شکل تو اسلاگ را درپست نمیفرستی !هرموقع ک با پست چیزی میفرستیم خودشم سیوش میکنه اما الان میکیم اقا بیا اینو خودت سیوش کن و یادبگیر
    def create(self, validated_data):
        product = Product(**validated_data)
        product.slug = slugify(product.name)  # Assign slug from the product name
        product.save()  # Save the product instance
        return product
    
    
class CommentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Comment
        fields = ['id', 'product', 'name', 'body',  'status']
from rest_framework import serializers
from .models import Cart, CartItem

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # مدل صحیح
        fields = ['id', 'name']
        
        
class AddCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']
# Include all relevant fields
class CartItemSerializer(serializers.ModelSerializer):
    #  product_name = serializers.ReadOnlyField(source='product.name') 
    #  product_name = serializers.StringRelatedField(source='product')
    product=ProductCartSerializer()
    item_total=serializers.SerializerMethodField()
    class Meta:
         model = CartItem
         fields = ['id', 'cart', 'product', 'quantity','item_total'] # Include all relevant fields
         
   
    def get_item_total(self, cart_item):
        return cart_item.quantity * cart_item.product.unit_price
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Define the relationship to CartItem
    total_price = serializers.SerializerMethodField() 
    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'items','total_price']  # Include the related items in the output
        read_only_fields = ['id','items']  # Make the 'id' field read-only
    def get_total_price(self, cart):
        # محاسبه مجموع قیمت کل سبد خرید
        return sum(item['item_total'] for item in CartItemSerializer(cart.items, many=True).data)  # جمع قیمت همه آیتم‌ها
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'phone_number', 'user']