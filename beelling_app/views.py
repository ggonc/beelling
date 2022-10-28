from django.shortcuts import render, redirect
from beelling_app.forms import BillForm
from beelling_app.models import Bill

# Create your views here.
def home(request):
    data = {}
    data['db'] = Bill.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = BillForm()
    return render(request, 'form.html', data)

def create(request):
    form = BillForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Bill.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Bill.objects.get(pk=pk)
    data['form'] = BillForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Bill.objects.get(pk=pk)
    form = BillForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Bill.objects.get(pk=pk)
    db.delete()
    return redirect('home')
