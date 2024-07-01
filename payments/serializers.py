from rest_framework import serializers
from .models import Payment
import django_filters


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentFilter(django_filters.FilterSet):
    sender_address = django_filters.CharFilter(lookup_expr="iexact")
    payment_type = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Payment
        fields = ["sender_address", "payment_type"]
