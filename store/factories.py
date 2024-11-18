import factory
from factory.django import DjangoModelFactory
from store.models import Category, Discount, Product, Customer, Address, Order, OrderItem, Comment, Cart, CartItem
from django.contrib.auth import get_user_model
from faker import Faker
import random

fake = Faker()

import factory
from django.contrib.auth import get_user_model
from faker import Faker

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    # Ensure the username is unique by appending a random number
    username = factory.LazyAttribute(lambda _: fake.user_name() + str(fake.random_number(digits=4)))
    
    # Ensure the email is unique by appending a random number to the email address
    email = factory.LazyAttribute(lambda _: fake.email().split('@')[0] + str(fake.random_number(digits=4)) + '@' + fake.email().split('@')[1])

    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
# Category Factory
class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda _: fake.sentence())

# Discount Factory
class DiscountFactory(DjangoModelFactory):
    class Meta:
        model = Discount

    discount = factory.LazyAttribute(lambda _: random.uniform(5, 50))
    description = factory.LazyAttribute(lambda _: fake.sentence())

# Product Factory
class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda _: fake.word())
    category = factory.SubFactory(CategoryFactory)
    slug = factory.LazyAttribute(lambda _: fake.slug())
    description = factory.LazyAttribute(lambda _: fake.text())
    unit_price = factory.LazyAttribute(lambda _: random.uniform(5, 100))
    inventory = factory.LazyAttribute(lambda _: random.randint(1, 100))

# Customer Factory
class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    user = factory.SubFactory(UserFactory)
    phone_number = factory.LazyAttribute(lambda _: fake.phone_number())
    birth_date = factory.LazyAttribute(lambda _: fake.date_of_birth())

# Address Factory
class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    customer = factory.SubFactory(CustomerFactory)
    province = factory.LazyAttribute(lambda _: fake.state())
    city = factory.LazyAttribute(lambda _: fake.city())
    street = factory.LazyAttribute(lambda _: fake.street_address())

# Order Factory
class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    status = factory.LazyAttribute(lambda _: random.choice([Order.ORDER_STATUS_UNPAID, Order.ORDER_STATUS_PAID, Order.ORDER_STATUS_CANCELED]))

# OrderItem Factory
class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.LazyAttribute(lambda _: random.randint(1, 5))
    unit_price = factory.LazyAttribute(lambda _: random.uniform(5, 100))

# Comment Factory
class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    product = factory.SubFactory(ProductFactory)
    name = factory.LazyAttribute(lambda _: fake.name())
    body = factory.LazyAttribute(lambda _: fake.text())
    status = factory.LazyAttribute(lambda _: random.choice([Comment.COMMENT_STATUS_WAITING, Comment.COMMENT_STATUS_APPROVED, Comment.COMMENT_STATUS_NOT_APPROVED]))

# Cart Factory
class CartFactory(DjangoModelFactory):
    class Meta:
        model = Cart

# CartItem Factory
class CartItemFactory(DjangoModelFactory):
    class Meta:
        model = CartItem

    cart = factory.SubFactory(CartFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.LazyAttribute(lambda _: random.randint(1, 5))
