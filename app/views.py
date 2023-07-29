import django_filters
from django.shortcuts import redirect
from rest_framework import generics, viewsets, filters
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


def index_view(request):
    redirect("products")


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ["name"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_class = ProductFilter
    search_fields = ["name"]


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by("id")
    serializer_class = StockSerializer
