
from rest_framework import serializers
from mummy_money.investors.models import Investor


class InvestorSerializer(serializers.HyperlinkedModelSerializer):
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
            'parent'
        )


class InvestorDetailSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')

    @staticmethod
    def get_children(self):
        if hasattr(self, "id"):
            queryset = Investor.objects.filter(parent_id=self.id)
            serializer = InvestorDetailSerializer(
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
