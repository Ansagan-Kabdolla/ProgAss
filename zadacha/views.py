from django.shortcuts import render,redirect
from .forms import EsepForm

def index(request):
    return render(request,'index.html')

def add_esep(request):
    if request.method == 'POST':
        form = EsepForm(request.POST, request.FILES)
        if form.is_valid:
            print(form)
            form.save()
    return redirect('index')