#create model forms
from django.forms import ModelForm
from .models import Cases

class CasesForm(ModelForm):
    class Meta:
        model = Cases
        fields = '__all__'
        