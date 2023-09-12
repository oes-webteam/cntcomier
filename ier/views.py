from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import DirectorateForm, HomeForm, UforceForm, PartnerForm, IerForm, UserinformationsForm, SignaturecentcomForm, SignaturepartnerForm, AddsubmissionForm
from .models import Directorate, Home, Addsubmission, Uforce, Partner, Ier, Userinformations, Signaturecentcom, Signaturepartner
from django.forms.models import model_to_dict

# Create your views here.


def homepage_view(request):
    submitted = False
    if request.method == 'GET':
        form = HomeForm
        return render(request, 'homepage.html', {'form': form, 'submitted': submitted})
    if request.method == 'POST':
        return HttpResponseRedirect('steps/1')


def addsubmission(request):
    submitted = False
    if request.method == 'POST':
        form = AddsubmissionForm(request.POST)
        if form.is_valid():
            form.save()
        submitted = True
    else:
        form = AddsubmissionForm()
        return render(request, 'ieraddsubmission.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('directorate')


def directorates_view(request):
    submitted = False
    if request.method == 'POST':
        form = DirectorateForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = DirectorateForm()
        return render(request, 'directorate.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('uforce')


def uforce(request):
    submitted = False
    if request.method == 'POST':
        form = UforceForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UforceForm()
        return render(request, 'uforce.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('partner')


def partner(request):
    submitted = False
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PartnerForm()
        return render(request, 'partner.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('ier_detail')


def ier_detail(request):
    submitted = False
    if request.method == 'POST':
        form = IerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = IerForm()
        return render(request, 'ier.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('userinfo')


def userinfo(request):
    submitted = False
    if request.method == 'POST':
        form = UserinformationsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserinformationsForm()
        return render(request, 'userinfo.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('signaturecentcom')


def partnersignature(request):
    submitted = False
    if request.method == 'POST':
        form = SignaturepartnerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignaturepartnerForm()
        return render(request, 'partnersignature.html', {'form': form, 'submitted': submitted})
    return HttpResponseRedirect('final')


def final(request):
    submitted = False
    if request.method == 'POST':
        form = SignaturecentcomForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        return render(request, 'final.html', {'submited': submitted})
    return HttpResponseRedirect('final')


STEPS = {
    1: {'form': 'AddsubmissionForm', 'page_title': 'Personal Information'},
    2: {'form': 'DirectorateForm', 'page_title': 'Directorate'},
    3: {'form': 'UforceForm', 'page_title': 'Uniform Member Information'},
    4: {'form': 'PartnerForm', 'page_title': 'Partner Nation(s)'},
    5: {'form': 'IerForm', 'page_title': 'Information Exchange Request Details'},
    6: {'form': 'UserinformationsForm', 'page_title': 'User Information'},
    7: {'form': 'SignaturecentcomForm', 'page_title': 'CENTCOM Signature'},
    8: {'form': 'SignaturepartnerForm', 'page_title': 'Partner Nation Signature'},
}

SESSIONKEY_PREFIX = 'submission_form'


def __getSessionData(request, step):
    '''Get session data for a step'''
    return request.session.get(SESSIONKEY_PREFIX + str(step))


def __getFormData(request, step):
    form = __getSessionData(request, step)
    return globals()[STEPS[step]['form']](form, initial=form)


def __setFormData(request, step, data):
    request.session[SESSIONKEY_PREFIX + str(step)] = data


def __getNextStep(request):
    for i in range(1, len(STEPS)):
        if __getSessionData(request, 1) == None:
            return 1
    return len(STEPS)


def FormView(request, step):
    '''multi steps form view'''
    if step == None:
        step = __getNextStep(request)
        return redirect('/steps/' + step)

    form = globals()[STEPS[step]['form']]()

    if request.method == 'POST':
        if step == len(STEPS):

            # savedaddsubmissionform = globals()[STEPS[1]['form']](request.POST)
            savedaddsubmissionform = __getFormData(request, 1)

            form = globals()[STEPS[step]['form']](request.POST)
            if form.is_valid():
                submission = None
                print('form_is_valid')
                existing_submissions = Addsubmission.objects.filter(
                    email_address=savedaddsubmissionform.instance.email_address)

                if existing_submissions.count() > 0:
                    submission = existing_submissions[0]
                    # Save Other Forms with the submission instance
                else:
                    submission = savedaddsubmissionform.save()
                    # submission = form.save()

                    # save store forms from session
                for i in range(2, len(STEPS)):
                    form_stored = __getFormData(request, i)
                    form_stored.instance.submission = submission
                    # print('form_index_is =' + 'i')
                    form_stored.save()

                form.instance.submission = submission

                request.session.flush()
                return render(request, 'final.html', {'submited': False})
        else:
            print('form_is_not_valid')
            form = globals()[STEPS[step]['form']](request.POST)

            if form.is_valid():
                __setFormData(request, step, model_to_dict(form.instance))
                return redirect('/steps/' + str(step+1))

    else:
        form = __getFormData(request, step)
    return render(request, 'form.html', {
        'form': form,
        'page_title': STEPS[step]['page_title'],
        'last_step': len(STEPS),
        'step': step
    })
