from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView
from .models import *
from .forms import CasesForm


# Create your views here.
class IndexPage(TemplateView):
    template_name = 'index.html'


class DisplayView(ListView):
    model = Cases
    template_name = 'display.html'


def casecreate(request):
    form =CasesForm
    if request.method == 'POST':
        form = CasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'newcases.html',context)
    

def caseupdate(request, pk):
    cases = Cases.objects.get(id=pk)
     

    form = CasesForm(instance=cases)
    if request.method == 'POST':
        form = CasesForm(request.POST, instance=cases)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, 'updatecases.html', context)

def casedelete(request, pk):
    cases = Cases.objects.get(id=pk)
    if request.method == "POST":
        cases.delete()
        return redirect('/')

    context ={'case': Cases}
    return render(request, 'deletecases.html', context)