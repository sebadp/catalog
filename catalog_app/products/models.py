from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ManyToManyField(Brand, related_name='products', blank=True)

    def __str__(self):
        return self.name

    def add_inventory(self, quantity):
        """
        Adds a quantity of items to the sku level for this product.
        """
        self.sku += quantity
        self.save()

    def remove_inventory(self, quantity):
        """
        Removes a quantity of items from the sku level for this product.
        """
        if self.sku < quantity:
            raise ValueError('Not enough inventory for this product.')
        self.sku -= quantity
        self.save()


class Query(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='queries')
    count = models.IntegerField()

    def __str__(self):
        return f"{self.product.name}: {self.count} queries"


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_group',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_perm',
        related_query_name='user',
    )
