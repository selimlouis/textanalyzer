from django.urls import path
from .views import (ReportDetailView, 
            ReportCreateView, 
            ReportUpdateView,
            ReportDeleteView
)



from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('info/', views.info, name="info"),
    path('report/<int:pk>/', ReportDetailView.as_view(), name="report-detail"),
    path('report/new/', ReportCreateView.as_view(), name="report-create"),
    path('report/<int:pk>/update/', ReportUpdateView.as_view(), name="report-update"),
    path('report/<int:pk>/delete/', ReportDeleteView.as_view(), name="report-delete")
]
