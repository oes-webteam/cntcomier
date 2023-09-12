from django import forms
from django.forms import ModelForm
from .models import Strategies, Addsubmission, Home

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


class StrategiesForm(ModelForm):
    class Meta:
        model = Strategies
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
            'product': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product'), ('Command Planning Board Plans Briefs and Updates', 'Command Planning Board Plans Briefs and Updates'), ('JSCP Plan IPR Briefs', 'JSCP Plan IPR Briefs'), ('Commander Directed Plan Briefings/ IPRs', 'Commander Directed Plan Briefings/ IPRs'), ('Library of Strategic Documents', 'Library of Strategic Documents'), ('Theater Strategy', 'Theater Strategy'), ('AOR Classified Brief', 'AOR Classified Brief')]),

            'rational': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Rational'), ('Obtain input, guidance, and/or approval from cross directorate planners and leadership regarding plans development', 'Obtain input, guidance, and/or approval from cross directorate planners and leadership regarding plans development'), ('Provide IPRs to Joint Staff and/or SECDEF regarding JSCP mandated plans', 'Provide IPRs to Joint Staff and/or SECDEF regarding JSCP mandated plans'), ('Provide IPRs to Command Group for input and/or approval', 'Provide IPRs to Command Group for input and/or approval'), ('Strategic Analysis Source', 'Strategic Analysis Source'), ('Strategic Planning', 'Strategic Planning'), ('Situational Awareness', 'Situational Awareness')]),

            'frequency': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Frequency'), ('Weekly', 'Weekly'), (
                'As scheduled', 'As scheduled'), ('As scheduled, directed, or required', 'As scheduled, directed, or required'), ('As Updated', 'As Updated')]),

            'format': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Format'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), (
                'Text, Graphics', 'Text, Graphics'), ('PPT', 'PPT')]),

            'sourcesofinput': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Sources of Input'), ('Staff planners from J5 and other directorates', 'Staff planners from J5 and other directorates'), ('Various', 'Various'), ('J5-ST and Cross Directorate', 'J5-ST and Cross Directorate')]),

            'means_info_extracted': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Means Info is extracted'), ('Planning team sessions, staff working groups', 'Planning team sessions, staff working groups'), ('CCJ5 Webpage', 'CCJ5 Webpage'), ('CCJ5 Webpage / Centcom Homepage', 'CCJ5 Webpage / Centcom Homepage'), ('CCJ5 Webpage (upon brief completion)', 'CCJ5 Webpage (upon brief completion)')]),


            'dissemination': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Dissemination'), ('Read aheads provided to session attendees, and briefings posted on SIPRNET R Drive', 'Read aheads provided to session attendees, and briefings posted on SIPRNET R Drive'), (
                'Deskside pre-brief to principle if requested', 'Deskside pre-brief to principle if requested'), ('Posted on CCJ5 Webpage', 'Posted on CCJ5 Webpage'), ('Brief', 'Brief')]),


            'primaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Primary Consumer'), ('Planners and leadership from directorates up to the Command Group', 'Planners and leadership from directorates up to the Command Group'), ('SECDEF, Joint Staff, CENTCOM CDR', 'SECDEF, Joint Staff, CENTCOM CDR'), ('Commander, DCOM, or COS', 'Commander, DCOM, or COS'), ('CENTCOM Components', 'CENTCOM Components'), ('CENTCOM Visitors', 'CENTCOM Visitors')]),

            'secondaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Secondary Consumer'), ('Staff Coalition and LNO Planners', 'Staff Coalition and LNO Planners'), ('Internal Planners', 'Internal Planners'), ('Others Components, Staff, JS, OSD', 'Others Components, Staff, JS, OSD'), ('CENTCOM Components, Others Components, Staff, JS, OSD', 'CENTCOM Components, Others Components, Staff, JS, OSD')]),

            'produceropr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OPR'), ('J5-P', 'J5-P'), ('J5-P or J3-P in support of CDR/ DCOM', 'J5-P or J3-P in support of CDR/ DCOM'), ('J5-P or J3-P', 'J5-P or J3-P'), ('Various', 'Various'), ('CENTCOM', 'CENTCOM'), ('CCJ5-ST', 'CCJ5-ST')]),

            'producerocr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OCR'), ('Various', 'Various'), ('CCJ1-8', 'CCJ1-8')]),

            'classification': forms.Select(attrs={'class': 'form-control'}, choices=[(
                '', 'Classification'), ('SECRET REL up to TS//NOFORN', 'SECRET REL up to TS//NOFORN'), ('S and Unclass', 'S and Unclass'), ('S', 'S')]),

            'policy_guidance_directive': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Policy Guidance / Directive'), ('Command Planning Board Charter (Draft in staffing)', 'Command Planning Board Charter (Draft in staffing)'), ('JSCP Guidance', 'JSCP Guidance'), ('Theater Campaign Plan, CDR/ DCOM Guidance', 'Theater Campaign Plan, CDR/ DCOM Guidance'), ('Various', 'Various')]),

            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here!'})

        }
