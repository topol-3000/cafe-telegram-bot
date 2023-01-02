from django.urls import path

from .views import (
    CustomerList,
    CustomerDetail,
    CustomerBalance,
)


app_name = "cafe"
urlpatterns = [
    path("customers/", CustomerList.as_view()),
    path("customers/<int:pk>/", CustomerDetail.as_view()),
    path("customers/<int:pk>/balance/", CustomerBalance.as_view()),
]
