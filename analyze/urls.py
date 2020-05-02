from django.urls import path
from .views import ReportDetailView, ReportCreateView



from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('report/<int:pk>/', ReportDetailView.as_view(), name="report-detail"),
    path('report/new/', ReportCreateView.as_view(), name="report-create"),
]
