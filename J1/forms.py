from django import forms
from django.forms import ModelForm
from .models import Humanresources, Addsubmission, Home


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
            'email_address')

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


class HumanresourcesForm(ModelForm):
    class Meta:
        model = Humanresources
        fields = [
            'product',
            'rational',
            'frequency',
            'format',
            'sourcesofinput',
            'meansofinfo',
            'dissemination',
            'primaryconsumer',
            'secondaryconsumer',
            'produceropr',
            'producerocr',
            'classification',
            'policyguidance',
            'note',
        ]

        labels = {
            'product': '',
            'rational': '',
            'frequency': '',
            'format': '',
            'sourcesofinput': '',
            'meansofinfo': '',
            'dissemination': '',
            'primaryconsumer': '',
            'secondaryconsumer': '',
            'produceropr': '',
            'producerocr': '',
            'classification': '',
            'policyguidance': '',
            'note': '',


        }

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product'), ('Cub, Maj Ops Slide', 'Cub, Maj Ops Slide'), ('Personnel strength changes - JPERSTAT', 'Personnel strength changes - JPERSTAT'), ('CENTCOM AOR Casualties Report- Active Cases ', 'CENTCOM AOR Casualties Report- Active Cases '), ('JTF Manning', 'JTF Manning')]),


            'rational': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Rational'), ('SA', 'SA'), ('Track changes in theater troop strength', 'Track changes in theater troop strength'), ('SA, Track, report trends analysis', 'SA, Track, report trends analysis'), ('S/A', 'S/A')]),


            'frequency': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Frequency'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('CENTCOM Components and JTF’s', 'CENTCOM Components and JTF’s')]),


            'format': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Format'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), ('Web page', 'Web page'), ('Web page, e-mail, PP slide', 'Web page, e-mail, PP slide'), ('Low', 'Low')]),

            'sourcesofinput': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Source of Input'), ('MNF-I, MNSTC-I', 'MNF-I, MNSTC-I'), ('Components', 'Components'), ('CAC Kuwait, SIGACT reports, Webpage BUA', 'CAC Kuwait, SIGACT reports, Webpage BUA'), ('N/A', 'N/A')]),

            'meansofinfo': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Means Information is Extracted'), ('SIGACTS Daily Reports, Updates', 'SIGACTS Daily Reports, Updates'), ('Web page, Email', 'Web page, Email'), (' Emails, SIGACTS', 'Emails, SIGACTS'), ('Monthly', 'Monthly')]),

            'dissemination': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product'), ('Briefing, Email, Posted on the Web, Archieve', 'Briefing, Email, Posted on the Web, Archieve'), ('Joint Staff, CCJ1, CDR, Components', 'Joint Staff, CCJ1, CDR, Components'), ('CCJ1, Joint Staff, CDR', 'CCJ1, Joint Staff, CDR'), ('CoS', 'CoS')]),

            'primaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Primary Consumers'), ('CDR ', 'CDR '), ('CDR, CCJ1', 'CDR, CCJ1'), ('CDR, CCJ1', 'CDR, CCJ1'), ('Text/Data', 'Text/Data')]),

            'secondaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Secondary Consumers'), ('Others Components, Staff, JS, OSD', 'Others Components, Staff, JS, OSD'), ('Joint Staff', 'Joint Staff'), ('SIPR', 'SIPR')]),

            'produceropr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OPR'), ('J3-O', 'J3-O'), ('CCJ1-XPO', 'CCJ1-XPO'), ('Email', 'Email')]),


            'producerocr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OCR'), ('J2, J5', 'J2, J5'), ('J3, J5, J2', 'J3, J5, J2'), ('Power Point Slides', 'Power Point Slides')]),

            'classification': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Classification'), ('TS', 'TS'), ('S', 'S'), ('U', 'U')]),

            'policyguidance': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Policyguidance'), ('IMP pg 34 IMP Appendix', 'IMP pg 34 IMP Appendix'), ('CJCSM 3150.13A', 'CJCSM 3150.13A'), ('CJCSM 3150.13A', 'CJCSM 3150.13A')]),

            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here!'})
        }
