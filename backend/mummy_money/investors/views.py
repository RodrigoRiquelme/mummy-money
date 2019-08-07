from django.db.models import F
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from mummy_money.investors.models import Investor
from mummy_money.investors.serializers import InvestorSerializer


# @permission_classes((IsAuthenticated,))
class PyramidViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

    def retrieve(self, request, pk=None):
        queryset = Investor.objects.all()
        investor = get_object_or_404(queryset, pk=pk)
        serializer = InvestorSerializer(investor)
        return Response(serializer.data)

    def perform_create(self, serializer):
        if self.request and hasattr(self.request, "data"):
            parent_id = self.request.data["parent"]

            parent = Investor.objects.filter(pk=parent_id)
            mummy = Investor.objects.filter(pk=1)

            if parent:
                parent.update(funds=F('funds') + 1000)
                mummy.update(funds=F('funds') + 1000)
            else:
                mummy.update(funds=F('funds') + 5000)

            serializer.save()
