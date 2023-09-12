from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm, AddsubmissionForm, LogisticForm
# Create your views here.


def jfourhomepage(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'jfourhomepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('jfourhomepage')


def addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'j4addsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('logistic')


def logistic(request):
    submitted = False
    if request.method == 'POST':
        form = LogisticForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = LogisticForm()
        return render(request, 'logistic.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    # submitted = False
    # if request.method == 'POST':
    #     return render(request, 'final.html', {'submited': submitted})
    return render(request, 'final.html/')
