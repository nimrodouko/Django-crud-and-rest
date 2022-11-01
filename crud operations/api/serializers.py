from rest_framework import serializers
from crudpages.models import *


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model= Cases
        fields =['Fullname', 'title', 'description',]