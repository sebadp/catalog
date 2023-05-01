from rest_framework import generics, permissions
from .models import Product, Brand, CustomUser, Query
from .permissions import AdminProductPermission
from .serializers import ProductSerializer, BrandSerializer, CustomUserSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 25


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, AdminProductPermission]
    pagination_class = ListPagination


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # check if the user is authenticated before creating/querying for a Query object
        if not self.request.user.is_authenticated:

            # Get or create the Query object for this product
            query, created = Query.objects.get_or_create(product=instance)

            # Increment the number of queries for this product
            query.count += 1
            query.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAdminUser]


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = ListPagination


class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = ListPagination


class CustomUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
