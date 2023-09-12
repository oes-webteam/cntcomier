from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm, AddsubmissionForm, JsevenForm
# Create your views here.


def jsevenhomepage(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'jsevenhomepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('jsevenhomepage')


def j7addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'j7addsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('jseven_training')


def training(request):
    submitted = False
    if request.method == 'POST':
        form = JsevenForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = JsevenForm()
        return render(request, 'training.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    # submitted = False
    # if request.method == 'POST':
    #     return render(request, 'final.html', {'submited': submitted})
    return render(request, 'final.html/')
