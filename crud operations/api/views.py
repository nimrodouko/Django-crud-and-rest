
from rest_framework import generics, permissions
from crudpages.models import *
from .serializers import CaseSerializer



class CaseApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cases.objects.all()
    serializer_class = CaseSerializer


class CaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cases.objects.all()
    serializer_class = CaseSerializer



