from django.core.management.base import BaseCommand
from store.factories import CategoryFactory, DiscountFactory, ProductFactory, CustomerFactory, AddressFactory, OrderFactory, OrderItemFactory, CommentFactory, CartFactory, CartItemFactory
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Generates fake data for the application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        # Here you can delete old data if needed
        # Category.objects.all().delete()
        # Product.objects.all().delete()
        # etc.

        self.stdout.write('Creating new data...')

        # Create Categories
        categories = CategoryFactory.create_batch(100)
        self.stdout.write(f'Added {len(categories)} categories...')

        # Create Discounts
        discounts = DiscountFactory.create_batch(10)
        self.stdout.write(f'Added {len(discounts)} discounts...')

        # Create Products
        products = ProductFactory.create_batch(1000)
        self.stdout.write(f'Added {len(products)} products...')

        # Create Customers
        customers = CustomerFactory.create_batch(500)
        self.stdout.write(f'Added {len(customers)} customers...')

        # Create Addresses for Customers
        addresses = AddressFactory.create_batch(500)
        self.stdout.write(f'Added {len(addresses)} addresses...')

        # Create Orders
        orders = OrderFactory.create_batch(1000)
        self.stdout.write(f'Added {len(orders)} orders...')

        # Create Order Items
        order_items = OrderItemFactory.create_batch(5000)
        self.stdout.write(f'Added {len(order_items)} order items...')

        # Create Comments
        comments = CommentFactory.create_batch(2000)
        self.stdout.write(f'Added {len(comments)} comments...')

        # Create Carts and Cart Items
        carts = CartFactory.create_batch(500)
        cart_items = CartItemFactory.create_batch(2500)
        self.stdout.write(f'Added {len(carts)} carts and {len(cart_items)} cart items...')

        self.stdout.write(self.style.SUCCESS('Successfully created fake data!'))
