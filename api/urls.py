from django.urls import path
from api import views

urlpatterns =[
    # path("product-list/",views.product_list, name="product_list"),
    path("product-list/",views.ProductListAPIView.as_view(), name="product_list"),
    # path("product-detail/<int:pk>",views.product_detail, name="product_detail"),
    path("product-detail/<int:product_id>",views.ProductDetailAPIView.as_view(), name="product_detail"),
    # path("order-list/",views.order_list, name="order_list"),
    path("order-list/",views.OrderListAPIView.as_view(), name="order_list"),
    path("product-info/",views.product_info, name="product_info"),

]
