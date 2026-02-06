from api.serializers import OrderSerializers, ProductInfoSerializers, ProductSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product, Order
from django.shortcuts import get_object_or_404
from django.db.models import Max
from rest_framework import generics

# Create your views here.


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.exclude(stock__gt=0)
    serializer_class = ProductSerializers


# @api_view(["GET"])
# def product_list(request):
#     products = Product.objects.all()
#     serializser = ProductSerializers(products, many=True)
#     return Response(serializser.data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_url_kwarg = "product_id"


# @api_view(["GET"])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializser = ProductSerializers(product)
#     return Response(serializser.data)


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("item__product")
    serializer_class = OrderSerializers


# @api_view(["GET"])
# def order_list(request):
#     orders = Order.objects.all()
#     serializser = OrderSerializers(orders, many=True)
#     return Response(serializser.data)


@api_view(["GET"])
def product_info(request):
    products = Product.objects.all()
    count = len(products)
    max_price = products.aggregate(max_price=Max("price"))["max_price"]
    serializser = ProductInfoSerializers(
        {"products": products, "count": count, "max_price": max_price}
    )
    return Response(serializser.data)
