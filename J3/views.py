from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm, AddsubmissionForm, OperationForm
# Create your views here.


def jthreehomepage(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'jthreehomepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('jthreehomepage')


def addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'j3addsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('ops')


def ops(request):
    submitted = False
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = OperationForm()
        return render(request, 'ops.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    # submitted = False
    # if request.method == 'POST':
    #     return render(request, 'final.html', {'submited': submitted})
    return render(request, 'final.html/')
