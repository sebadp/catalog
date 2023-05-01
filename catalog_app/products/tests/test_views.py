from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from products.models import CustomUser, Brand, Product, Query


class ProductTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_superuser(
            username='testuser', email='test@example.com', password='testpassword')
        self.brand = Brand.objects.create(name='Test Brand')
        self.product = Product.objects.create(
            sku=1234,
            name='Test Product',
            price=9.99,
            description='Test Description',
        )
        self.product.brand.add(self.brand)

    def test_create_product_unauthenticated(self):
        url = reverse('product_list_create')
        data = {
            'sku': 5678,
            'name': 'New Product',
            'price': 4.99,
            'description': 'New Description',
            'brand': [self.brand.id],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_product_authenticated(self):
        url = reverse('product_list_create')
        data = {
            'sku': 5678,
            'name': 'New Product',
            'price': 4.99,
            'description': 'New Description',
            'brand': [self.brand.id],
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_product_unauthenticated(self):
        url = reverse('product_retrieve_update_destroy', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test incrementing query count
        query_count = Query.objects.get(pk=self.product.id).count
        expected_querys = 1
        self.assertEqual(expected_querys, query_count)

    def test_update_product(self):
        url = reverse('product_retrieve_update_destroy', args=[self.product.id])
        data = {
            'sku': 1234,
            'name': 'Updated Product',
            'price': 14.99,
            'description': 'Updated Description',
            'brand': [self.brand.id],
        }
        self.client.force_authenticate(self.user)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        url = reverse('product_retrieve_update_destroy', args=[self.product.id])
        self.client.force_authenticate(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
