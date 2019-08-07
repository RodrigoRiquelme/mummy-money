
from rest_framework import serializers
from mummy_money.investors.models import Investor


class InvestorSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')

    @staticmethod
    def get_children(self):
        if hasattr(self, "id"):
            queryset = Investor.objects.filter(parent_id=self.id)
            serializer = InvestorSerializer(
                instance=queryset.all(),
                many=True
            )
            return serializer.data
        else:
            return []

    class Meta:
        model = Investor
        fields = (
            'id',
            'name',
            'funds',
            'innocence',
            'experience',
            'charisma',
            'status',
            'joining_at',
            'leaving_at',
            'parent',
            'children'
        )
