from django import forms
from django.forms import ModelForm
from .models import Operation, Addsubmission, Home

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


class OperationForm(ModelForm):
    class Meta:
        model = Operation
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
            'product': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product'), ('CUB Maritime focus area', 'CUB Maritime focus area'), ('OPS and INTEL Brief Maritime update', 'OPS and INTEL Brief Maritime update'), (
                'Retrieving data. Wait a few seconds and try to cut or copy again', 'Retrieving data. Wait a few seconds and try to cut or copy again'), ('TLAM Status', 'TLAM Status'), ('Marine Expeditionary Unit (MEU) Commitment', 'Marine Expeditionary Unit (MEU) Commitment'), ('5th Fleet Scheme of Maneuver', '5th Fleet Scheme of Maneuver'), ('Coalition Scheme of Maneuver', 'Coalition Scheme of Maneuver'), ('Operational Weather Update', 'Operational Weather Update'), ('CDR Travel Weather', 'CDR Travel Weather'), ('Recon 4 Msgs', 'Recon 4 Msgs'), ('Recon 3 Msgs', 'Recon 3 Msgs'), ('Monthly Allocation Directive', 'Monthly Allocation Directive'), ('Air Order of Battle', 'Air Order of Battle'), ('Daily Boardwalk Brief', 'Daily Boardwalk Brief'), ('Daily ATO Strike Summary', 'Daily ATO Strike Summary'), ('Monthly ATO Strike Summary', 'Monthly ATO Strike Summary'), ('SNR Weekly Strike Rollup', 'SNR Weekly Strike Rollup'), ('SNR Monthly Strike Rollup', 'SNR Monthly Strike Rollup'), ('CENTCOM SITREP', 'CENTCOM SITREP'), ('ATO Weekly Sortie Summary', 'ATO Weekly Sortie Summary'), ('HOA/OEF/OIF Monthly Sortie Summary', 'HOA/OEF/OIF Monthly Sortie Summary'), ('CUB CAS (AFG) focus area', 'OPS and INTEL Brief CAS (AFG) update'), ('SNR (AFG) focus area', 'SNR (AFG) focus area'), ('Component Commaders Brief', 'Component Commaders Brief'), ('CUB AP (IRQ) focus area', 'CUB AP (IRQ) focus area'), ('OPS and INTEL Brief AP (IRQ) update', 'OPS and INTEL Brief AP (IRQ) update'), ('SNR (IRQ) focus area', 'SNR (IRQ) focus area'), ('Component Commaders Brief', 'Component Commaders Brief')]),

            'rational': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Rational'), ('SA', 'SA'), ('ISR mission tracking', 'ISR mission tracking'), (
                'ISR requirements tracking', 'ISR requirements tracking'), ('Situational Awareness', 'Situational Awareness')]),

            'frequency': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Frequency'), ('Daily', 'Daily'), (
                'Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('As Required', 'As Required'), ('Bimonthly', 'Bimonthly'), ('By Event', 'By Event'), ('As Reqd', 'As Reqd'), ('Situational', 'Situational')]),

            'format': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Frequency'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), ('PPT/text to First Look', 'PPT/text to First Look'), ('Text to First Look', 'Text to First Look'), ('Msg Format', 'Msg Format'), ('Excel', 'Excel'), ('High', 'High')]),

            'sourcesofinput': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Source Of Input')]),

            'meansofinfo': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Means Information is Extracted'), ('Web page', 'Web page'), ('Email Web page', 'Email Web page'), ('Joint Operations Area Forecast', 'Joint Operations Area Forecast'), (
                'Operational Weather Websites', 'Operational Weather Websites'), ('E-mail/ Websked/ ROME', 'E-mail/ Websked/ ROME'), ('E-mail/ Tasker-Tool', 'E-mail/ Tasker-Tool'), ('CFACC, MNF-I, NAVCENT, MARCENT', 'CFACC, MNF-I, NAVCENT, MARCENT'), ('AUAB CAOC', 'AUAB CAOC'), ('CFACC, NAVCENT', 'CFACC, NAVCENT'), ('AUAB CAOC', 'AUAB CAOC'), ('Numerous', 'Numerous'), ('PP submission via Email ', 'PP submission via Email '), ('Email, Web page, CIDNE', 'Email, Web page, CIDNE')]),


            'dissemination': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Dissemination'), ('Briefing, Email, Posted on the Web, Archive', 'Briefing, Email, Posted on the Web, Archive'), ('Briefing/Input to CHOPS First Look', 'Briefing/Input to CHOPS First Look'), ('Input to CHOPS First Look', 'Input to CHOPS First Look'), ('JS', 'JS'), ('CCJ3, Components', 'CCJ3, Components'), (
                'E-mail, Portal', 'E-mail, Portal'), ('E-mail', 'E-mail')]),


            'primaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Primaryconsumer'), (
                'CDR ', 'CDR '), ('J3/J2', 'J3/J2'), ('CCC', 'CCC'), ('J3', 'J3'), ('Components', 'Components'), ('Text, Graphics', 'Text, Graphics')]),

            'secondaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Secondary Consumer'), ('J3/J2', 'J3/J2'), ('JOC', 'JOC'), ('N/A', 'N/A'), (
                'Theater METOC Personnel', 'Theater METOC Personnel'), ('HQ Staff', 'HQ Staff'), ('COCOM, Joint Staff', 'COCOM, Joint Staff'), ('COCOM', 'COCOM'), ('CCJ3', 'CCJ3')]),

            'produceropr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OPR'), (
                'J3-O', 'J3-O'), ('NAVCENT', 'NAVCENT'), ('J3-O-ISR', 'J3-O-ISR'), ('CENTCOM, Components, JS', 'CENTCOM, Components, JS')]),

            'producerocr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product OCR'), ('J2, J5', 'J2, J5'), ('J3-O', 'J3-O'), (
                'N/A', 'N/A'), ('28th OWS, Shaw AFB', '28th OWS, Shaw AFB'), ('None', 'None'), ('Components', 'Components'), ('CAS Air Desk', 'CAS Air Desk')]),

            'classification': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Classification'), ('S/FVEY', 'S/FVEY'), ('S/NOFORN', 'S/NOFORN'), ('S/GCTF', 'S/GCTF'), ('S/GBR', 'S/GBR'), ('S/REL GCTF', 'S/REL GCTF'), ('S', 'S'), ('S/ISAF NATO', 'S/ISAF NATO')]),

            'policyguidance': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Policy Guidance / Directive'), (
                'Local SOP', 'Local SOP'), ('CJCSI', 'CJCSI'), ('CENTCOM J3', 'CENTCOM J3'), ('S/Rel AUS, GBR', 'S/Rel AUS, GBR'), ('S/Rel ISAF, NATO', 'S/Rel ISAF, NATO'), ('S/Rel AUS, CAN, GBR', 'S/Rel AUS, CAN, GBR'), ('S/Rel ISAF, NATO', 'S/Rel ISAF, NATO'), ('S/Rel AUS, CAN, GBR', ''), ('CCJ3-JOC Battlebook ', 'CCJ3-JOC Battlebook ')]),

            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here!'})

        }
