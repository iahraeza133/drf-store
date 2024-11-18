from django.contrib import admin
from .models import Product, Category, Order
from .models import Comment
from django.db.models import Count
from django.contrib import admin
from .models import Order, OrderItem,Cart
from django.contrib import admin
from .models import Order, OrderItem
from django.contrib import admin
from .models import Product, Category, CartItem 
from django.contrib import admin
from .models import Customer
# فیلتر سفارشی موجودی

class CommentInline(admin.TabularInline):  # یا admin.StackedInline
    model = Comment
    extra = 0  # تعداد فیلدهای اضافی که به صورت پیش‌فرض نمایش داده شوند
    readonly_fields = ('name', 'body', 'status')  # فیلدهای فقط خواندنی
    fields = ('name', 'body', 'status')
class InventoryFilter(admin.SimpleListFilter):
    title = 'Critical Inventory'  # عنوان فیلتر
    parameter_name = 'inventory'  # نام پارامتر که در URL استفاده می‌شود

    def lookups(self, request, model_admin):
        # تعریف گزینه‌های فیلتر
        return (
            ('low', 'Low Inventory'),  # نمایش موجودی کم
            ('out_of_stock', 'Out of Stock')  # نمایش موجودی تمام شده
        )

    def queryset(self, request, queryset):
        # اعمال فیلتر بر اساس انتخاب کاربر
        value = self.value()
        if value == 'low':
            return queryset.filter(inventory__lt=10)  # محصولات با موجودی کمتر از 10
        if value == 'out_of_stock':
            return queryset.filter(inventory=0)  # محصولات بدون موجودی
        return queryset

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_price', 'inventory_status', 'category_status')
    search_fields = ('name',)
    list_editable = ['unit_price']
    inlines = [CommentInline] 
    list_per_page = 10
    list_filter = ( InventoryFilter,)  # اضافه کردن فیلتر سفارشی و دسته‌بندی
    list_select_related = ['category']
    prepopulated_fields={
        'slug':['name']
    }
    autocomplete_fields = ['category',]
    # Custom display method for inventory status
    def inventory_status(self, obj):
        if obj.inventory > 10:
            return "Normal Inventory"
        elif obj.inventory < 10:
            return "Low Inventory"
        elif obj.inventory < 1:
            return "Out of Stock"
    inventory_status.admin_order_field = 'inventory'  # This allows sorting by inventory
    inventory_status.short_description = 'Inventory Status'  # Custom header for the column

    # Display the category title for category status
    @admin.display(ordering='category__title')
    def category_status(self, obj):
        return obj.category.title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'top_product')
    search_fields=["title"]
from django.db.models import Count
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity', 'unit_price']
    extra = 1
    readonly_fields = ['unit_price']
    min_num = 1
    max_num = 10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'status', 'customer_birth_date', 'num_of_order')
    search_fields = ('status',)
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10
    inlines = [OrderItemInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # استفاده از select_related به جای prefetch_related برای کاهش تعداد کوئری‌ها
        return queryset.select_related('customer', 'customer__user').annotate(items_count=Count('items'))

    @admin.display(ordering='items_count')
    def num_of_order(self, obj):
        return obj.items.count()  # تعداد آیتم‌ها در سفارش

    num_of_order.short_description = 'Number of Items'

    @admin.display(description='Customer Name')
    def customer_name(self, obj):
        return obj.customer.user.first_name  # دسترسی به نام مشتری

    @admin.display(description='Customer Birth Date')
    def customer_birth_date(self, obj):
        return obj.customer.birth_date  # دسترسی به تاریخ تولد مشتری

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name' ,'product_inventory')
    search_fields = ('product__name',)  # جستجو بر اساس نام محصول و نام کاربری کاربر
    list_filter = ('datetime_created',)

    # نمایش نام محصول
    @admin.display(description='Product Name')
    def product_name(self, obj):
        return obj.product.name  # درست کردن دسترسی به نام محصول

    def product_inventory(self,obj):
        return obj.product.inventory  # درست کردن دسترسی به تعداد موجودی محصول
    
from django.contrib import admin
from .models import OrderItem

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'quantity', 'unit_price')
    search_fields = ('product__name',)  # جستجو بر اساس نام محصول
    list_filter = ('order__status',)    # فیلتر بر اساس وضعیت سفارش
    list_select_related = ('product', 'order')  # استفاده از select_related برای کاهش تعداد درخواست‌ها

    def product_name(self, obj):
        return obj.product.name  # دسترسی به نام محصول از طریق ارتباط ForeignKey با مدل Product

    product_name.admin_order_field = 'product__name'  # امکان مرتب‌سازی بر اساس نام محصول
    product_name.short_description = 'Product Name'   # عنوان نمایش داده شده برای این فیلد
    


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # مشخص کردن فیلدهایی که در صفحه مدیریت نمایش داده می‌شوند
    list_display = ('user', 'phone_number', 'birth_date','first_name','last_name')
    ordering = ['user__first_name', 'user__last_name']
    # فیلدهایی که برای جستجو در پنل مدیریت استفاده می‌شوند
    search_fields = ('user__username', 'phone_number')
    
    # فیلدهایی که می‌توانند برای فیلتر در پنل مدیریت استفاده شوند
    list_filter = ('birth_date',)
    autocomplete_fields = ('user',)
    
    # تنظیمات پیشرفته برای نحوه نمایش اطلاعات
    def __str__(self):
        return self.user.username  # نمایش نام کاربری کاربر مربوطه به‌عنوان نام نمایشی    @admin.display(description='First Name')  # عنوان برای ستون first_name
    @admin.display(description='First Name', ordering='user__first_name')  # مرتب‌سازی براساس first_name
    def first_name(self, obj):
        return obj.user.first_name

    @admin.display(description='Last Name', ordering='user__last_name')  # مرتب‌سازی براساس last_name
    def last_name(self, obj):
        return obj.user.last_name

    
class CartItemInline(admin.TabularInline):  # Or use `admin.StackedInline` for a different layout
    model = CartItem
    extra = 1  # Nc
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    inlines = [CartItemInline]