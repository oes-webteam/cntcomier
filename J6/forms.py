from django import forms
from django.forms import ModelForm
from .models import J6, Addsubmission, Home

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


class J6Form(ModelForm):
    class Meta:
        model = J6
        fields = [
            'product',
            'rational',
            'frequency',
            'format',
            'sourcesofinput',
            # 'means_info_extracted',
            'dissemination',
            'primaryconsumer',
            # 'secondaryconsumer',
            'produceropr',
            # 'producerocr',
            'classification',
            'policy_guidance_directive',
            'note',

        ]

        labels = {
            'Product': '',
            'rational': '',
            'frequency': '',
            'sourcesofinput': '',
            # 'means_info_extracted': '',
            'dissemination': '',
            'primaryconsumer': '',
            # 'secondaryconsumer': '',
            'produceropr': '',
            # 'producerocr': '',
            'classification': '',
            'policy_guidance_directive': '',
            'note': '',



        }

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Product'), ('Information Assurance Incident report', 'Information Assurance Incident report'), ('Circuit Outage Report (COMSTAT)', 'Circuit Outage Report (COMSTAT)'), ('COMSEC incident report', 'COMSEC incident report'), ('Switch Outage (COMSTAT)', 'Switch Outage (COMSTAT)'), ('Component SITREP, OPREP, OPSUM, SIR/CRITIC, SPOTREP', 'Component SITREP, OPREP, OPSUM, SIR/CRITIC, SPOTREP'), ('Commanders SITREP', 'Commanders SITREP'), ('Coalition/Combined Force Status', 'Coalition/Combined Force Status'), ('CCIR, JQRR', 'CCIR, JQRR'), ('CCIR', 'CCIR'), ('COP', 'COP'), ('INTSUM', 'INTSUM'), ('Air Tasking Order/Airspace Control Order', 'Air Tasking Order/Airspace Control Order'), ('CJCS Warning/Alert Order, CJCS Strategic Assessment', 'CJCS Warning/Alert Order, CJCS Strategic Assessment'), ('Coalition Forces SITREP', 'Coalition Forces SITREP'), ('OPREP-1 (Eval Request), CJCS Warning/Alert Order', 'OPREP-1 (Eval Request), CJCS Warning/Alert Order'), ('OPREP-1 (Commander(s) Estimate)', 'OPREP-1 (Commander(s) Estimate)'), ('Resource Information (Allocation, Apportionment, Allotment, Availability, Assignment)', 'Resource Information (Allocation, Apportionment, Allotment, Availability, Assignment)'), ('Issued OPLAN, CONPLAN, OPORD, TPFDD LOI, JCEOI, FRAGO, CDR(s) ROE', 'Issued OPLAN, CONPLAN, OPORD, TPFDD LOI, JCEOI, FRAGO, CDR(s) ROE'), ('C2-related Information ', 'C2-related Information '), ('ROE', 'ROE'), ('Targeting Guidance,  CFC CONOP, Weight of Effort, OPLAN, OPORD, FRAGO, ROE, Target Selection, Target Prioritization, ATO Information', 'Targeting Guidance,  CFC CONOP, Weight of Effort, OPLAN, OPORD, FRAGO, ROE, Target Selection, Target Prioritization, ATO Information'), ('Target Policy and Objectives', 'Target Policy and Objectives'), ('Collateral Damage Guidance', 'Collateral Damage Guidance'), ('FSCL Guidance/Information', 'FSCL Guidance/Information'), ('FSCL Recommendation/Information', 'FSCL Recommendation/Information'), ('FSCL Information', 'FSCL Information'), ('Target Information, Target Lists, Target Dbase', 'Target Information, Target Lists, Target Dbase'), ('Target Information, Target Lists', 'Target Information, Target Lists'), ('Monitor/assess/execute time-sensitive targeting events', 'Monitor/assess/execute time-sensitive targeting events'), ('ATO Information', 'ATO Information'), ('BDA Reports', 'BDA Reports'), ('WMD Launch Information', 'WMD Launch Information'), ('6110.01 Request (JCSE), ', '6110.01 Request (JCSE),'), ('JCSE  Deployment Order', 'JCSE  Deployment Order'), ('GAR, SAR, FREQ Request, NARC Activation Msg, ACP 117 Mod Msg', 'GAR, SAR, FREQ Request, NARC Activation Msg, ACP 117 Mod Msg'), ('SAA, TSO', 'SAA, TSO'), ('JCEOI, TSO ', 'JCEOI, TSO '), ('COMSTAT Report', 'COMSTAT Report'), ('C4ISR Network Management Information', 'C4ISR Network Management Information'), ('C4ISR Network Monitoring and reporting, security alerts, compromise reports, event data, event logs', 'C4ISR Network Monitoring and reporting, security alerts, compromise reports, event data, event logs'), ('Coalition Coordination', 'Coalition Coordination'), ('Collection Asset Status, Component RFI', 'Collection Asset Status, Component RFI'), ('CDRs PRs, National Collection Requests, CDRs PIR', 'CDR(s) PRs, National Collection Requests, CDR(s) PIR'), ('USCENTCOM Collection Plan', 'USCENTCOM Collection Plan'), ('Raw Intelligence Data', 'Raw Intelligence Data'), ('U.S. Collection Results rept', 'U.S. Collection Results rept'), ('Coalition Gathered Intelligence Rept', 'Coalition Gathered Intelligence Rept'), ('Intelligence/Intelligence Products ', 'Intelligence/Intelligence Products ')]),

            'rational': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Rationale'), ('Protection of Networks', 'Protection of Networks'), ('Repair communication system', 'Repair communication system'), ('Alert to possible compromise of protected systems', 'Alert to possible compromise of protected systems'), (
                'Repair voice communication system', 'Repair voice communication system'), ('SECDEF Visibility During General Elections;  Vote Impact', 'SECDEF Visibility During General Elections;  Vote Impact'), ('Recovery and Reporting Mandated by DoD; CDR & Public Visibility', 'Recovery and Reporting Mandated by DoD; CDR & Public Visibility')]),

            'frequency': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Frequency'), ('By Event', 'By Event'), (
                'Daily', 'Daily'), ('Monthly', 'Monthly'), ('Bi-Weekly', 'Bi-Weekly'), ('Weekly', 'Weekly')]),

            'format': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Format'), ('Voice, Message, Text,  Data', 'Voice, Message, Text,  Data'), ('Message, Voice', 'Message, Voice'), ('Message', 'Message'), ('Data', 'Data'), ('Message, Text', 'Message, Text'), ('Message, Video', 'Message, Video'), ('Message, Voice, Video', 'Message, Voice, Video'), (
                'Message, Data, Voice, Video', 'Message, Data, Voice, Video'), ('Hard copy, Email, Message', 'Hard copy, Email, Message'), ('Data, Voice, Message Traffic, Web Products', 'Data, Voice, Message Traffic, Web Products'), ('Data, Voice, Message Traffic, Web Products', 'Data, Voice, Message Traffic, Web Products'), ('Message Traffic; J6 PIR Log Entry', 'Message Traffic; J6 PIR Log Entry')]),

            'sourcesofinput': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Sources of Input'), ('Components, JTF, Defense Agencies, Coalition', 'Components, JTF, Defense Agencies, Coalition'), ('Components, JTF, Defense Agencies', 'Components, JTF, Defense Agencies'), ('Components, Joint Service Functional Elements', 'Components, Joint Service Functional Elements'), ('USCENTCOM (REAR), CFH ', 'USCENTCOM (REAR), CFH '), ('Coalition/Combined Force HQ', 'Coalition/Combined Force HQ'), ('USCENTCOM (REAR), CFH', 'USCENTCOM (REAR), CFH'), ('USCENTCOM (REAR), USCENTCOM HQ, CFH, C/JTF', 'USCENTCOM (REAR), USCENTCOM HQ, CFH, C/JTF'), ('USCENTCOM JIC', 'USCENTCOM JIC'), ('CFACC', 'CFACC'), ('JCS', 'JCS'), ('Components, C/JTF, Defense Agencies', 'Components, C/JTF, Defense Agencies'), ('CF Staff, Components, F2C2', 'CF Staff, Components, F2C2'), ('Components, Joint Service Functional Elements, JTF', 'Components, Joint Service Functional Elements, JTF'), ('NCA', 'NCA'), ('JTCB', 'JTCB'), ('Components', 'Components'), ('Components, DOCC, JTCB, F2C2 ', 'Components, DOCC, JTCB, F2C2 '), ('USCENTCOM (REAR), CFH, Components/JTF(s)', 'USCENTCOM (REAR), CFH, Components/JTF(s)'), ('CFACC', 'CFACC'), ('NIMA', 'NIMA'), ('S&R Sensors', 'S&R Sensors'), ('DISA', 'DISA'), ('DISA, DIA, Components, Joint Service Functional Elements', 'DISA, DIA, Components, Joint Service Functional Elements'), ('NMCC, USSPACECOM, DISA, RNOSC, CERTs/CIRTs, Components, Joint Service Functional Elements', 'NMCC, USSPACECOM, DISA, RNOSC, CERTs/CIRTs, Components, Joint Service Functional Elements'), ('Components, Joint Service Functional Elements (Intelligence)', 'Components, Joint Service Functional Elements (Intelligence)'), ('USCENTCOM JIC (REAR), USCENTCOM JIC, C/JTF JIC', 'USCENTCOM JIC (REAR), USCENTCOM JIC, C/JTF JIC'), ('Tactical, Theater, and National Collection assets', 'Tactical, Theater, and National Collection assets'), ('U.S. Collection Units/Assets', 'U.S. Collection Units/Assets'), ('Coalition Collection Units/Assets', 'Coalition Collection Units/Assets'), ('U.S. Collection Units/Assets, USCENTCOM JIC', 'U.S. Collection Units/Assets, USCENTCOM JIC'), ('U.S. and Coalition Collection Units/Assets', 'U.S. and Coalition Collection Units/Assets'), ('USCENTCOM JIC, CFACC (Primarily via Combined/Coalition Data Network [C/CDN])', 'USCENTCOM JIC, CFACC (Primarily via Combined/Coalition Data Network [C/CDN])'), ('Component and Field Postal Activities thru the SSM to J6', 'Component and Field Postal Activities thru the SSM to J6')]),

            # 'means_info_extracted': forms.Select(attrs={'class': 'form-control'}, choices=[]),


            'dissemination': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Dissemination'), ('Varied by format', 'Varied by format')]),


            'primaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Primary Consumer'), ('USCENTCOM HQ, CFH, C/JTF, DISA, JTF-GNO', 'USCENTCOM HQ, CFH, C/JTF, DISA, JTF-GNO'), ('TCCC, RNOSC', 'TCCC, RNOSC'), ('USCENTCOM HQ, CFH, JS', 'USCENTCOM HQ, CFH, JS'), ('USCENTCOM (REAR), USCENTCOM HQ, CFH, C/JTF', 'USCENTCOM (REAR), USCENTCOM HQ, CFH, C/JTF'), ('SECDEF, CJCS, Components', 'SECDEF, CJCS, Components'), ('USCENTCOM (REAR), CFH', 'USCENTCOM (REAR), CFH'), ('Components, Joint Service Functional Elements, JIC', 'Components, Joint Service Functional Elements, JIC'), ('Coalition Force HQ', 'Coalition Force HQ'), ('USCENTCOM (REAR), CFH, Components', 'USCENTCOM (REAR), CFH, Components'), ('CFH, USCENTCOM (REAR), Components, C/JTFs, Coalition NCC/PJHQs, Air Units', 'CFH, USCENTCOM (REAR), Components, C/JTFs, Coalition NCC/PJHQs, Air Units'), ('JCS', 'JCS'), ('CF Staff, Components, F2C2', 'CF Staff, Components, F2C2'), ('Components, Joint Service Functional Elements, C/JTF', 'Components, Joint Service Functional Elements, C/JTF'), ('Components, Joint Service Functional Elements, C/JTF, CF Staff, F2C2, JTWG', 'Components, Joint Service Functional Elements, C/JTF, CF Staff, F2C2, JTWG'), ('POTUS, SECDEF, NMJIC, DOCC, Components', 'POTUS, SECDEF, NMJIC, DOCC, Components'), ('Components', 'Components'), ('Components, DOCC, JTCB, CF Staff, F2C2 ', 'Components, DOCC, JTCB, CF Staff, F2C2'), ('USCENTCOM (REAR), CFH, Components/JTFs', 'USCENTCOM (REAR), CFH, Components/JTFs'), ('F2C2', 'F2C2'), ('NMJIC', 'NMJIC'), ('JCS, USCFCOM', 'JCS, USCFCOM'), ('DISA', 'DISA'), ('Components, Joint Service Functional Elements ', 'Components, Joint Service Functional Elements '), ('DISA, DIA, Components, Joint Service Functional Elements', 'DISA, DIA, Components, Joint Service Functional Elements'), ('NMCC, USSPACECOM, DISA, RNOSC, CERTs/CIRTs, Components, Joint Service Functional Elements', 'NMCC, USSPACECOM, DISA, RNOSC, CERTs/CIRTs, Components, Joint Service Functional Elements'), ('Coalition Force', 'Coalition Force'), ('USCENTCOM JIC (REAR), USCENTCOM JIC, C/JTF JIC', 'USCENTCOM JIC (REAR), USCENTCOM JIC, C/JTF JIC'), ('National Intelligence Community', 'National Intelligence Community'), ('CJTFs, Combat Forces, CFACC, CMFCC, CFLCC, USCENTCOM JIC, Other Combatant Commands, National Authorities', 'CJTFs, Combat Forces, CFACC, CMFCC, CFLCC, USCENTCOM JIC, Other Combatant Commands, National Authorities'), ('CJTFs, Combat Forces, CFACC, CMFCC, CFLCC, USCENTCOM JIC, Other Combatant Commands, National Authorities, Coalition Forces', 'CJTFs, Combat Forces, CFACC, CMFCC, CFLCC, USCENTCOM JIC, Other Combatant Commands, National Authorities, Coalition Forces'), ('Coalition Force HQ', 'Coalition Force HQ'), ('CJTFs, Commanders, Mail Transportation Managers, J6 & J4', 'CJTFs, Commanders, Mail Transportation Managers, J6 & J4')]),

            # 'secondaryconsumer': forms.Select(attrs={'class': 'form-control'}, choices=[]),

            'produceropr': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Producer OPR'), ('Components, JTF, Defense Agencies, Coalition', 'Components, JTF, Defense Agencies, Coalition'), ('Components, JTF, Defense Agencies', 'Components, JTF, Defense Agencies'), ('Components, Joint Service Functional Elements', 'Components, Joint Service Functional Elements'), ('USCENTCOM (REAR), CFH ', 'USCENTCOM (REAR), CFH '), ('Coalition/Combined Force HQ', 'Coalition/Combined Force HQ'), ('USCENTCOM (REAR), CFH', 'USCENTCOM (REAR), CFH'), ('USCENTCOM (REAR), USCENTCOM HQ, CFH, C/JTF', 'USCENTCOM (REAR), USCENTCOM HQ, CFH, C/JTF'), ('USCENTCOM JIC', 'USCENTCOM JIC'), ('CFACC', 'CFACC'), ('JCS', 'JCS'), ('Components, Joint Service Functional Elements', 'Components, Joint Service Functional Elements'), ('Coalition Force HQ', 'Coalition Force HQ'), ('CF Staff, Components, F2C2', 'CF Staff, Components, F2C2'), ('Components, Joint Service Functional Elements, JTF', 'Components, Joint Service Functional Elements, JTF'), ('NCA', 'NCA'), ('JTCB', 'JTCB'), ('Components', 'Components'), ('Components, DOCC, JTCB, F2C2 ', 'Components, DOCC, JTCB, F2C2 '), ('NIMA', 'NIMA'), ('S&R Sensors', 'S&R Sensors'), ('CJCS', 'CJCS'), ('DISA', 'DISA'), ('USCENTCOM (REAR), USCENTCOM HQ, C/JTF', 'USCENTCOM (REAR), USCENTCOM HQ, C/JTF'), ('Components, C/JTF', 'Components, C/JTF'), ('DISA, DIA, Components, Joint Service Functional Elements', 'DISA, DIA, Components, Joint Service Functional Elements'), ('NMCC, USSPACECOM, DISA, RNOSC, CERTs/CIRTs, Components, Joint Service Functional Elements', 'NMCC, USSPACECOM, DISA, RNOSC, CERTs/CIRTs, Components, Joint Service Functional Elements'), ('Tactical, Theater, and National Collection assets', 'Tactical, Theater, and National Collection assets'), ('U.S. Collection Units/Assets', 'U.S. Collection Units/Assets'), ('Coalition Collection Units/Assets', 'Coalition Collection Units/Assets'), ('U.S. Collection Units/Assets, USCENTCOM JIC', 'U.S. Collection Units/Assets, USCENTCOM JIC'), ('USCENTCOM JIC, CFACC (Primarily via Combined/Coalition Data Network [C/CDN])', 'USCENTCOM JIC, CFACC (Primarily via Combined/Coalition Data Network [C/CDN])'), ('Component and Field Postal Activities thru the SSM to J6', 'Component and Field Postal Activities thru the SSM to J6')]),

            # 'producerocr': forms.Select(attrs={'class': 'form-control'}, choices=[]),

            'classification': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Classification'), ('S/TS', 'S/TS'), ('S', 'S'), ('Collateral ', 'Collateral '), ('Collateral, TS/SCI', 'Collateral, TS/SCI'), ('Rel Collateral', 'Rel Collateral'), (
                'Collateral, TS/SCI', 'Collateral, TS/SCI'), ('Collateral, TS/SCI', 'Collateral, TS/SCI'), ('SCI, Collateral', 'SCI, Collateral'), ('SCI, Collateral, Releasable Collateral', 'SCI, Collateral, Releasable Collateral')]),

            'policy_guidance_directive': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Policy Guidance / Directive'), ('CCR 25-206', 'CCR 25-206'), (
                'Service COMSEC regulations', 'Service COMSEC regulations'), ('CCR 25-102, J6 CCIR/PIR Policy', 'CCR 25-102, J6 CCIR/PIR Policy')]),

            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here!'})

        }
