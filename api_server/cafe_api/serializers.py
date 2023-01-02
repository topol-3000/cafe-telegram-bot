from rest_framework.serializers import ModelSerializer
from .models.users import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "first_name", "last_name", "phone_number"]


class CustomerBalanceSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["balance"]
