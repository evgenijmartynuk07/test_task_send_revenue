from django.urls import path
from revenue import views

urlpatterns = [
    path("", views.RevenueStatisticView.as_view(), name="revenue-statistic"),
]

app_name = "revenue"
