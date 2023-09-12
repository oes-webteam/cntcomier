from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm, AddsubmissionForm, IntellForm
# Create your views here.


def jtwohomepage(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'jtwohomepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('jtwohomepage')


def addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'j2addsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('intell')


def intell(request):
    submitted = False
    if request.method == 'POST':
        form = IntellForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = IntellForm()
        return render(request, 'intell.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    # submitted = False
    # if request.method == 'POST':
    #     return render(request, 'final.html', {'submited': submitted})
    return render(request, 'final.html/')
