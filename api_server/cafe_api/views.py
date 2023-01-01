from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import Http404
from .models.users import Customer
from .serializers import CustomerSerializer, CustomerBalanceSerializer


class CustomerList(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerBalance(APIView):
    def get(self, _request: Request, pk: int) -> Response:
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

        serializer = CustomerBalanceSerializer(customer)
        return Response(serializer.data)
