from django.urls import  path
from .views import *
from . import views


urlpatterns=[
    path('', IndexPage.as_view(), name='index'),
    path('display/', DisplayView.as_view(),name='display'),
    path('casecreate/',views.casecreate, name='casecreate' ),
    path('caseupdate/<str:pk>/',views.caseupdate, name='caseupdate' ),
    path('casedelete/<str:pk>/',views.casedelete, name='casedelete' ),
]   