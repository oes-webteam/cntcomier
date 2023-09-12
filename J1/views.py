from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm, HumanresourcesForm, AddsubmissionForm
# Create your views here.


def jonehomepage(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'jonehomepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('jonehomepage')


def addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'j1addsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('humanresources')


def humanresources(request):
    submitted = False
    if request.method == 'POST':
        form = HumanresourcesForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = HumanresourcesForm()
        return render(request, 'humanresources.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    # submitted = False
    # if request.method == 'POST':
    #     return render(request, 'final.html', {'submited': submitted})
    return render(request, 'final.html/')

    # if request.method == 'POST':
    #     product = ProductForm(request.POST, prefix='Product')
    #     rational = RationalForm(request.POST, prefix='Rational')
    #     frequency = FrequencyForm(request.POST, prefix='Frequency')
    #     format = FormatForm(request.POST, prefix='Product')
    #     sourcesofinput = SourcesofinputForm(
    #         request.POST, prefix='Sourcesofinput')
    #     meansofinfo = MeansofinfoForm(request.POST, prefix='Meansofinfo')
    #     dissemination = DisseminationForm(request.POST, prefix='Dissemination')
    #     primaryconsumer = PrimaryconsumerForm(
    #         request.POST, prefix='Meansofinfo')
    #     secondaryconsumer = SecondaryconsumerForm(
    #         request.POST, prefix='Secondaryconsumer')
    #     produceropr = ProduceroprForm(request.POST, prefix='Produceropr')
    #     producerocr = ProducerocrForm(request.POST, prefix='Producerocr')
    #     classification = ClassificationForm(
    #         request.POST, prefix='Classification')
    #     policyguidance = PolicyguidanceForm(
    #         request.POST, prefix='Policyguidance')
