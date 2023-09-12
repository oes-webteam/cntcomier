# from django import forms
# from django.forms import ModelForm
# from .models import Venue, Event

from django import forms
from django.forms import ModelForm
from .models import Directorate, Home, Addsubmission, Uforce, Partner, Ier, Userinformations, Signaturecentcom, Signaturepartner

#  HOMEPAGE BLOCK CODES


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

# END OF HOMEPAGE

# START OF ADDSUBMISSION BLOCK CODES


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

        # field_order = [
        #     'fname',
        #     'lname',
        #     'location',
        #     'phone',
        #     'email_address',
        # ]

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
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }

    # def __int__(self, *args, **kwargs):
    #     super(AddsubmissionForm, self).__int__(*args, **kwargs)
    #     self.fields.keyOrder = ['fname',
    #                             'lname',
    #                             'location',
    #                             'phone',
    #                             'email_address']


# END OF ADDSUBMISSION BLOCK
# START OF DIRECTORATE


class DirectorateForm(ModelForm):
    class Meta:
        model = Directorate
        fields = [
            'directorate',
            'service_branch',
            'poc_name',
            'poc_email',
            'poc_phone',
        ]

        labels = {
            'directorate': '',
            'service_branch': '',
            'poc_name': '',
            'poc_email': '',
            'poc_phone': '',
        }

        widgets = {
            'directorate': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Select Directorate'), ('J1', 'J1'), ('J2', 'J2'), ('J3', 'J3'), ('J4', 'J4'), ('J5', 'J5'), ('J6', 'J6'), ('J7', 'J7'), ('J8', 'J8')]),
            'service_branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service / Branch'}),
            'poc_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Directorate Point of Contact First & Last Name'}),
            'poc_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Directorate Point of Contact Email Address'}),
            'poc_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Directorate Point of Contact Phone'}),
        }


# END OF DIRECTORATE

# START OF UFORCE


class UforceForm(ModelForm):
    class Meta:
        model = Uforce
        fields = ['service_branch',
                  'command_unit',
                  'office_code',
                  'poc_lname',
                  'poc_fname',
                  'poc_phone',
                  'poc_email',]

        labels = {
            'service_branch': '',
            'command_unit': '',
            'office_code': '',
            'poc_lname': '',
            'poc_fname': '',
            'poc_phone': '',
            'poc_email': '',
        }

        widgets = {
            'service_branch': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Service Branch'}),
            'command_unit': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Command Unit'}),
            'office_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Office Code'}),
            'poc_lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Point  Of Contact  Last Name'}),
            'poc_fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Point  Of Contact First  Name'}),
            'poc_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Point of Contact Phone Number'}),
            'poc_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Point  of Contact Email'}),
        }


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ['service_branch',
                  'command_unit',
                  'office_code',
                  'poc_lname',
                  'poc_fname',
                  'poc_phone',
                  'poc_email',]

        labels = {
            'service_branch': '',
            'command_unit': '',
            'office_code': '',
            'poc_lname': '',
            'poc_fname': '',
            'poc_phone': '',
            'poc_email': '',
        }

        widgets = {
            'service_branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Branch'}),
            'command_unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Command / Unit'}),
            'office_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Office Code'}),
            'poc_lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Point  Of Contact Last Name'}),
            'poc_fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Point  Of Contact  First Name'}),
            'poc_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Point ofContact Phone Number'}),
            'poc_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Point  of Contact Email'}),
        }


class IerForm(ModelForm):
    class Meta:
        model = Ier
        fields = ['information_ype', 'purpose', 'ion', 'ops_impact',
                  'information_type', 'fore_m', 'data_format', 'waveform',
                  'transport_path', 'on_data', 'on_data', 'release',
                  'frequency', 'duration', 'reference', 'additional_information'
                  ]

        labels = {
            'information_ype': '',
            'purpose': '',
            'justification': '',
            'ops_impact': '',
            'information_type': '',
            'fore_m': '',
            'data_format': '',
            'waveform': '',
            'transport_path': '',
            'on_data': '',
            'release': '',
            'frequency': '',
            'duration': '',
            'reference': '',
            # 'upload': '',
            'additional_information': '',
        }

        widgets = {
            'information_ype': forms.Select(attrs={'class': 'form-control'}),

            'purpose': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purpose'}),

            'justification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Justification'}),

            'ops_impact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Operational Impact if this IER is Not Met'}),

            'information_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Information Type'}),

            'fore_m': forms.Select(attrs={'class': 'form-control'}),

            'data_format': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data Format (If applicable)'}),

            'waveform': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Waveform(s) (If applicable)'}),

            'transport_path': forms.Select(attrs={'class': 'form-control'}),

            'on_data': forms.Select(attrs={'class': 'form-control'}),

            'release': forms.Select(attrs={'class': 'form-control'}),

            'frequency': forms.Select(attrs={'class': 'form-control'}),

            'duration': forms.Select(attrs={'class': 'form-control'}),

            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference(s)'}),

            # 'upload': forms.FileInput(attrs={'class': 'form-control', 'multiple': True, 'placeholder': 'Upload', 'required': None}),

            'additional_information': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Information'}),
        }


class UserinformationsForm(ModelForm):
    class Meta:
        model = Userinformations
        fields = [
            'platform_type',
            'capability_name',
            'sender_node',
            'receiver_node',
            'intermediate_node',
            'architecture_ov1',
            'equipment_information',
            'general_location',
            'cross_cocom',
            'position',
            'organization',
        ]

        labels = {
            'platform_type': '',
            'capability_name': '',
            'sender_node': '',
            'receiver_node': '',
            'intermediate_node': '',
            'architecture_ov1': '',
            'equipment_information': '',
            'general_location': '',
            'cross_cocom': '',
            'position': '',
            'organization': '',
            # 'date': '',
        }

        widgets = {
            'platform_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Platform Type(s) by Domain'}),

            'capability_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Capability Name'}),

            'sender_node': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sender Node(s)'}),

            'receiver_node': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Receiver Node(s)'}),

            'intermediate_node': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Intermediate Node'}),

            'architecture_ov1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Architecture OV1'}),

            'equipment_information': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Equipment Information'}),

            'general_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AOR/General Location'}),

            'cross_cocom': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cross COCOM'}),

            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),

            'organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization'}),

            # 'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),




        }


class SignaturecentcomForm(ModelForm):
    class Meta:
        model = Signaturecentcom
        fields = ['name',
                  'position',
                  'organization',
                  ]

        labels = {
            'name': '',
            'position': '',
            'organization': '',
            # 'date': ''
        }

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization'}),
            # 'date': forms.DateTimeField(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        }


class SignaturepartnerForm(ModelForm):
    class Meta:
        model = Signaturepartner
        fields = ['name',
                  'position',
                  'organization',
                  ]

        labels = {
            'name': '',
            'position': '',
            'organization': '',
            # 'date': ''
        }

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization'}),
            # 'date': forms.DateTimeField(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        }
