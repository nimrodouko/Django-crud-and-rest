from django.urls import path
from .views import *

urlpatterns =[
    path('',CaseApiView.as_view()),
    path('<int:pk>/', CaseDetailView.as_view()),
]
