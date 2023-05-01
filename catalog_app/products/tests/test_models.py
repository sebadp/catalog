from django.test import TestCase

from products.models import Brand, Product, Query, CustomUser


class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name='Brand1')

    def test_name_label(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_name(self):
        brand = Brand.objects.get(id=1)
        expected_object_name = brand.name
        self.assertEquals(expected_object_name, str(brand))


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Product1', price=10.0, description='Test description')

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = product.name
        self.assertEquals(expected_object_name, str(product))

    def test_add_inventory(self):
        product = Product.objects.get(id=1)
        sku_before_add = product.sku
        product.add_inventory(10)
        sku_after_add = product.sku
        self.assertEquals(sku_before_add + 10, sku_after_add)

    def test_remove_inventory(self):
        product = Product.objects.get(id=1)
        product.sku = 15
        product.save()
        sku_before_remove = product.sku
        product.remove_inventory(5)
        sku_after_remove = product.sku
        self.assertEquals(sku_before_remove - 5, sku_after_remove)

    def test_remove_inventory_error(self):
        product = Product.objects.get(id=1)
        product.sku = 5
        product.save()
        with self.assertRaises(ValueError):
            product.remove_inventory(10)


class QueryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        brand = Brand.objects.create(name='Brand1')
        product = Product.objects.create(name='Product1', price=10.0, description='Test description')
        product.brand.add(brand)
        Query.objects.create(product=product, count=5)

    def test_object_name_is_name(self):
        query = Query.objects.get(id=1)
        expected_object_name = f'{query.product.name}: {query.count} queries'
        self.assertEquals(expected_object_name, str(query))


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(username='user1', password='password1')

    def test_username_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_username_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 150)

    def test_object_name_is_username(self):
        user = CustomUser.objects.get(id=1)
        user.username
