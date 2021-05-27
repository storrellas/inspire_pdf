from django.urls import path

from django.views.generic import TemplateView
from .views import MedicalExpertPDFExportView

urlpatterns = [
    path('', MedicalExpertPDFExportView.as_view()),
]