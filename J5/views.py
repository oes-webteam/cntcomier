from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm, AddsubmissionForm, StrategiesForm


def jfivehomepage(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'jfivehomepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('jfivehomepage')


def addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'j5addsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('strategies')


def strategies(request):
    submitted = False
    if request.method == 'POST':
        form = StrategiesForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = StrategiesForm()
        return render(request, 'strategies.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    # submitted = False
    # if request.method == 'POST':
    #     return render(request, 'final.html', {'submited': submitted})
    return render(request, 'final.html/')
