from django import forms
from django.forms import ModelForm
from .models import Jseven, Addsubmission, Home

# HOME PAGE


class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = ('description', 'start')

        label = {
            'description': '',
        }

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }

# ADDSUBMISSION FORM


class AddsubmissionForm(ModelForm):
    class Meta:
        model = Addsubmission

        fields = (

            'fname',
            'lname',
            'location',
            'phone',
            'email_address',
        )

        labels = {
            'fname': '',
            'lname': '',
            'location': '',
            'phone': '',
            'email_address': ''
        }

        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Location'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }
# PRODUCT FORM


class JsevenForm(ModelForm):
    class Meta:
        model = Jseven
        fields = [
            'product',
            'rational',
            'frequency',
            'format',
            'sourcesofinput',
            'means_info_extracted',
            'dissemination',
            'primaryconsumer',
            'secondaryconsumer',
            'produceropr',
            'producerocr',
            'classification',
            'policy_guidance_directive',
            'note',

        ]

        labels = {
            'product': '',
            'rational': '',
            'frequency': '',
            'format': '',
            'sourcesofinput': '',
            'means_info_extracted': '',
            'dissemination': '',
            'primaryconsumer': '',
            'secondaryconsumer': '',
            'produceropr': '',
            'producerocr': '',
            'classification': '',
            'policy_guidance_directive': '',
            'note': '',



        }

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product'), ('Commander Weekly Update', 'Commander Weekly Update'), ('Significant Military Exercise Breif', 'Significant Military Exercise Breif'), ('Information Papers', 'Information Papers'), ('Defense Readiness Report System (DRRS) Update', 'Defense Readiness Report System (DRRS) Update'), ('JS J7 & CoS Updates', 'JS J7 & CoS Updates')]),

            'rational': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Rational'), ('SA', 'SA'), ('JS Requirement', 'JS Requirement'), ('JS and CoS Requirement', 'JS and CoS Requirement')]),

            'frequency': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Frequency'), ('Weekly', 'Weekly'), ('As Required', 'As Required'), ('Monthly', 'Monthly'), ('Daily', 'Daily')]),

            'format': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Format'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), ('Text', 'Text'), ('PPT', 'PPT')]),

            'sourcesofinput': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Sources of Input'), ('Internal Reporting', 'Internal Reporting'), ('Unit, Component, Internal Reporting', 'Unit, Component, Internal Reporting'), ('Unit Reporting', 'Unit Reporting'), ('Collections Reporting', 'Collections Reporting')]),

            'means_info_extracted': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Means Info is extracted'), ('websites, email, databases', 'websites, email, databases'), ('AMHS, Secure Phone, Email', 'AMHS, Secure Phone, Email')]),


            'dissemination': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Dissemination'), ('Email', 'Email'), (
                'Email, Electronic Staff Package (ESP), Message', 'Email, Electronic Staff Package (ESP), Message'), ('Email, Web', 'Email, Web')]),


            'primaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Primary Consumer'), ('CDR', 'CDR'), ('CJCS', 'CJCS'), ('CDR and Directors', 'CDR and Directors'), ('CENTCOM Joint Staff', 'CENTCOM Joint Staff'), ('J7', 'J7')]),

            'secondaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Secondary Consumer'), ('Others, Components, JTFs & Coalition Forces', 'Others, Components, JTFs & Coalition Forces'), ('J7 Staff', 'J7 Staff')]),

            'produceropr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OPR'), ('J7-E, J7-P, J7-T', 'J7-E, J7-P, J7-T'), ('J7-E', 'J7-E'), ('J7-TR', 'J7-TR')]),

            'producerocr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OCR'), ('N/A', 'N/A')]),

            'classification': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Classification'), ('SECRET REL up to TS//NOFORN', 'SECRET REL up to TS//NOFORN'), ('S and Unclass', 'S and Unclass'), ('S', 'S'), ('Multiple', 'Multiple'), ('S and Below', 'S and Below')]),

            'policy_guidance_directive': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Policy Guidance / Directive'), ('N/A', 'N/A')]),

            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here!'})

        }
