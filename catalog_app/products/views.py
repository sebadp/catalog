from rest_framework import generics, permissions
from .models import Product, Brand, CustomUser, Query
from .permissions import AdminProductPermission
from .serializers import ProductSerializer, BrandSerializer, CustomUserSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ListPagination(PageNumberPagination):
    """
    Custom pagination class for product, brand, and user lists.

    page_size: int
        Default number of items per page.

    page_size_query_param: str
        The name of the query parameter used to set the size of a page.

    max_page_size: int
        Maximum number of items that can be returned per page.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 25


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint that allows the creation and listing of products.

    queryset: QuerySet
        List of all Product objects sorted by id.

    serializer_class: Serializer
        Serializer class used to serialize and deserialize Product objects.

    permission_classes: list
        List of permission classes that authenticate and authorize access to this view.

    pagination_class: Pagination
        Class used to paginate the results.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, AdminProductPermission]
    pagination_class = ListPagination


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows the retrieval, updating, and deletion of a specific product.

    queryset: QuerySet
        List of all Product objects.

    serializer_class: Serializer
        Serializer class used to serialize and deserialize Product objects.

    permission_classes: list
        List of permission classes that authenticate and authorize access to this view.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves the details of a specific product.

        If the user is not authenticated, creates or retrieves a Query object for this product and increments the number of queries.
        """
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
    """
        API endpoint that allows the retrieval, updating, and deletion of a specific brand.

        queryset: QuerySet
            List of all Brand objects.

        serializer_class: Serializer
            Serializer class used to serialize and deserialize Brand objects.

        permission_classes: list
            List of permission classes that authenticate and authorize access to this view.
        """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAdminUser]


class BrandListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint that allows the creation and listing of brands.

    queryset: QuerySet
        List of all Brand objects sorted by id.

    serializer_class: Serializer
        Serializer class used to serialize and deserialize Brand objects.

    permission_classes: list
        List of permission classes that authenticate and authorize access to this view.

    pagination_class: Pagination
        Class used to paginate the results.
    """
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = ListPagination


class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint that allows the creation and listing of users.
    """
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = ListPagination


class CustomUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows the retrieval, updating, and deletion of a specific user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
