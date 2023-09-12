from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm, AddsubmissionForm, J6Form
# Create your views here.


def jsixhomepage(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'jsixhomepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('jsixhomepage')


def j6addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'j6addsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('jsix_comm')


def comm(request):
    submitted = False
    if request.method == 'POST':
        form = J6Form(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = J6Form()
        return render(request, 'comm.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    # submitted = False
    # if request.method == 'POST':
    #     return render(request, 'final.html', {'submited': submitted})
    return render(request, 'final.html/')
