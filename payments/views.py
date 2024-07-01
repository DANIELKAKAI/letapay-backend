from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Payment
from .serializers import PaymentSerializer, PaymentFilter
from .tasks import schedule_task_at_specific_time


class PaymentsView(ListCreateAPIView):
    queryset = Payment.objects.order_by("-payment_datetime").all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        schedule_task_at_specific_time(
            str(serializer.instance.payment_id),
            serializer.instance.payment_datetime,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class PaymentDetailView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = "payment_id"
