from django.db.models import Sum
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RevenueStatistic


class RevenueStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = "__all__"


class RevenueStatisticView(APIView):
    serializer_class = RevenueStatisticSerializer

    def get(self, request):
        queryset = RevenueStatistic.objects.values("name", "date").annotate(
            total_revenue=Sum("revenue"),
            total_spend=Sum("spend__spend"),
            total_impressions=Sum("spend__impressions"),
            total_clicks=Sum("spend__clicks"),
            total_conversion=Sum("spend__conversion")
        )

        return Response(queryset)
