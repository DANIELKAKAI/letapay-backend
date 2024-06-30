from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Payment
from .serializers import PaymentSerializer


class PaymentsView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = "payment_id"
