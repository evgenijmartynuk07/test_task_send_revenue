from django.urls import path
from spend import views

urlpatterns = [
    path('', views.SpendStatisticView.as_view(), name='spend-statistic'),
]

app_name = "spend"
