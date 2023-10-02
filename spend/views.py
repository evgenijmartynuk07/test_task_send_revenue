from django.db.models import Sum, Subquery, OuterRef
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from revenue.models import RevenueStatistic
from .models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = "__all__"


class SpendStatisticView(APIView):
    serializer_class = SpendStatisticSerializer

    def get(self, request):
        revenue_subquery = RevenueStatistic.objects.filter(
            spend=OuterRef("pk")
        ).values("spend").annotate(
            total_revenue=Sum("revenue")
        ).values("total_revenue")[:1]

        queryset = SpendStatistic.objects.values("name", "date").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
            total_revenue=Subquery(revenue_subquery)
        )

        return Response(queryset)
