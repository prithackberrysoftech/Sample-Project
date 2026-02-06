from rest_framework import serializers
from api.models import Product, Order, OrderItem


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "price", "stock")


    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price Must be Grether than 0")


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(max_digits=5, decimal_places=2, source='product.price')

    class Meta:
        model = OrderItem
        fields = (  
            "product_name",
            "product_price",
            "quantity",
            "item_subtotal",
        )


class OrderSerializers(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(
        method_name="total"
    )  # by defalut get_name_of_variable but you can modify name also like total

    class Meta:
        model = Order
        fields = (
            "order_id",
            "user",
            "created_at",
            "status",
            "product",
            "items",
            "total_price",
        )

    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)


class ProductInfoSerializers(serializers.Serializer):
    products = ProductSerializers(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()

