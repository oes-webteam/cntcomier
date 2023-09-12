from django import forms
from django.forms import ModelForm
from .models import Logistic, Addsubmission, Home

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


class LogisticForm(ModelForm):
    class Meta:
        model = Logistic
        fields = [
            'product',
            'rational',
            'frequency',
            'format',
            'sourcesofinput',
            'meansinfoextracted',
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
            'meansinfoextracted': '',
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
            'product': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product'), ('Engineer SITREP', 'Engineer SITREP'), ('MPL & CPL submissions', 'MPL & CPL submissions'), ('OEF/OIF Air Munitions Expenditure', 'OEF/OIF Air Munitions Expenditure'), (
                'Ground Ammunition Status ', 'Ground Ammunition Status'), ('AOR Fuel Supply Status  ', 'AOR Fuel Supply Status'), ('Mortuary Affairs', 'Mortuary Affairs'), ('Contractor Census', 'Contractor Census'), ('Daily Update Report', 'Daily Update Report')]),

            'rational': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Rational'), ('Situational Awareness', 'Situational Awareness'), (
                'SA, JS requirement', 'SA, JS requirement'), ('SA', 'SA')]),

            'frequency': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Frequency'), ('Ea FRI', 'Ea FRI'), (
                'As Directed', 'As Directed'), ('Daily', 'Daily'), ('Quarterly', 'Quarterly')]),

            'format': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Format'), ('Text, Excel', 'Text, Excel'), (
                'Text, Excel', 'Text, Excel'), ('Text', 'Text'), ('Text/Powerpoint', 'Text/Powerpoint'), ('Excel via email and internet', 'Excel via email and internet')]),

            'sourcesofinput': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Sources of Input'), (
                'Components, JTFs', 'Components, JTFs'), ('CFACC, CFMCC', 'CFACC, CFMCC'), ('Joint Mortuary Affairs (Services)', 'Joint Mortuary Affairs (Services)'), ('Service Components and Services', 'Service Components and Services'), ('CJTF-101, MNC-I, CFLCC, CFACC, CFMCC, DESC-ME SITREP, Truck Report', 'CJTF-101, MNC-I, CFLCC, CFACC, CFMCC, DESC-ME SITREP, Truck Report')]),

            'meansinfoextracted': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Means Info is extracted'), ('Submitted Reports', 'Submitted Reports'), ('EMAILS, WEB PAGE', 'EMAILS, WEB PAGE'), (
                'Web-based/excel REPOL & DESC reports', 'Web-based/excel REPOL & DESC reports'), ('Manual', 'Manual '), ('Electronic via internet and email', 'Electronic via internet and email')]),


            'dissemination': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Dissemination'), ('Email', 'Email'), ('Web Page, Joint Total Access Visibility (JTAV)', 'Web Page, Joint Total Access Visibility (JTAV)'), (
                'Email,  Web page, AMHS', 'Email,  Web page, AMHS'), ('Email, Web page', 'Email, Web page'), ('Web page ', 'Web page'), ('OSD, Joint Staff', 'OSD, Joint Staff'), ('Via email, CENTCOM webpage.', 'Via email, CENTCOM webpage.')]),


            'primaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Primary Consumer'), ('CENTCOM', 'CENTCOM'), ('JS, CCJ4-O', 'JS, CCJ4-O'), ('CCJ4-O', 'CCJ4-O'), ('CCJ4-C', 'CCJ4-C'), ('CDR', 'CDR')]),

            'secondaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Secondary Consumers'), ('N/A', 'N/A'), ('OSD, Service Components', 'OSD, Service Components'), ('J4 DIRECTOR/DEP DIRECTOR, J3 DIRECTOR/DEP DIRECTOR, J3-O-CAS , J4-O, JCS SJS, JCS J4/SD', 'J4 DIRECTOR / DEP DIRECTOR, J3 DIRECTOR/DEP DIRECTOR, J3-O-CAS , J4-O, JCS SJS, JCS J4/SD'), ('ARCENT, TRANSCOM, DESC, 1st TSC, CDDOC, DLA, JCS, EUCOM JPO, TACC, AFPET, AALOCSM, MNC-I, 101st SBDE, MNF-I, CJTF-101, 165th QM GP, 311th ESC, 3rd ESC, 16th SB, HQDA', 'ARCENT, TRANSCOM, DESC, 1st TSC, CDDOC, DLA, JCS, EUCOM JPO, TACC, AFPET, AALOCSM, MNC-I, 101st SBDE, MNF-I, CJTF-101, 165th QM GP, 311th ESC, 3rd ESC, 16th SB, HQDA'), ('OSD', 'OSD'), ('Others Components, Staff, JS, OSD', 'Others Components, Staff, JS, OSD')]),

            'produceropr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OPR'), ('CCJ4-E', 'CCJ4-E'), ('Components, JTFs', 'Components, JTFs'), ('Service Components', 'Service Components'), ('CCJ4-OJMO', 'CCJ4-OJMO'), ('CCJ4-OJPO', 'CCJ4-OJPO'), ('CCJ4-C', 'CCJ4-C')]),

            'producerocr': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Producer OCR'), ('N/A', 'N/A'), ('DESC, MNC-I, AFCENT, CJTF-101, 311th ESC, 165th QM GP', 'DESC, MNC-I, AFCENT, CJTF-101, 311th ESC, 165th QM GP'), ('Service Components and Services', 'Service Components and Services')]),

            'classification': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Classification'), ('S/Rel ', 'S/Rel '), ('FOUO', 'FOUO'), ('Unclass', 'Unclass'), ('Secret', 'Secret')]),

            'policy_guidance_directive': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Policy Guidance Directive'), (
                'CCR 415-1', 'CCR 415-1'), ('DoD Instruction US Code', 'DoD Instruction US Code'), ('MUREP REPORTING  FOR 1003V from JSJ4', 'MUREP REPORTING  FOR 1003V from JSJ4'), ('No policy, guidance, directive. Produced only as directed.', 'No policy, guidance, directive. Produced only as directed.'), ('DODI 3020.41/CENTCOM FRAGO', 'DODI 3020.41/CENTCOM FRAGO'), ('Joint Publication 4-03: Joint Bulk Petroleum and Water Doctrine.  CCJ4-JPO Local Policy', 'Joint Publication 4-03: Joint Bulk Petroleum and Water Doctrine.  CCJ4-JPO Local Policy')]),

            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here!'})

        }
