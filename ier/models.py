from django.db import models
from datetime import date


class Home(models.Model):
    description = models.TextField()
    start = models.TextField()

    class Meta:
        verbose_name = "home"

        verbose_name_plural = "home"

    def __str__(self):
        return self.description


class Addsubmission(models.Model):
    fname = models.CharField('First Names', max_length=50)
    lname = models.CharField('Last Name', max_length=50)
    location = models.CharField('Location of submission', max_length=150)
    phone = models.CharField('Phone Number', max_length=25, blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    class Meta:
        verbose_name = "Addsubmission"

        verbose_name_plural = "Addsubmissions"

    def __str__(self):
        return self.fname + ' ' + self.lname


class Directorate(models.Model):
    directorate = models.CharField(
        'Select Directorate', max_length=250, choices=[('', 'Select Directorate'), ('J1', 'J1'), ('J2', 'J2'), ('J3', 'J3'), ('J4', 'J4'), ('J5', 'J5'), ('J6', 'J6'), ('J7', 'J7'), ('J8', 'J8')])
    service_branch = models.CharField(
        'Service Branch', max_length=50)
    poc_name = models.CharField(
        'Directorate Point of Contact First & Last Name', max_length=500)
    poc_email = models.EmailField(
        'Directorate Point of Contact Email Address')
    poc_phone = models.CharField(
        'Directorate Point of Contact Phone Number', max_length=15)
    submission = models.OneToOneField(
        Addsubmission, on_delete=models.CASCADE, primary_key=True, default=1)

    class Meta:
        verbose_name = "Directorate"

        verbose_name_plural = "Directorates"

    def __str__(self):
        return self.poc_name


class Uforce(models.Model):
    service_branch = models.CharField(
        'Service Branch', max_length=250, choices=[('', 'Service Branch'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU')])
    command_unit = models.CharField(
        'Command/Unit/Organization', max_length=250, choices=[('', 'Command / Unit'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU'), ('UUUU', 'UUUU')])
    office_code = models.CharField('Office Code', max_length=250)
    poc_lname = models.CharField('Last Name', max_length=250)
    poc_fname = models.CharField('First Name', max_length=250)
    poc_phone = models.CharField('POC Phone Number', max_length=250)
    poc_email = models.EmailField('POC Email', max_length=250)
    submission = models.OneToOneField(
        Addsubmission, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "Uforce"

        verbose_name_plural = "Uforces"

    def __str__(self):
        return self.poc_lname + ' ' + self.poc_fname


class Partner(models.Model):
    service_branch = models.CharField('Service Branch', max_length=250)
    command_unit = models.CharField(
        'Command/Unit/Organization', max_length=250)
    office_code = models.CharField('Office Code', max_length=250)
    poc_lname = models.CharField('POC Name', max_length=250)
    poc_fname = models.CharField('POC Name', max_length=250)
    poc_phone = models.CharField('POC Phone Number', max_length=250)
    poc_email = models.EmailField('POC Email', max_length=250)
    submission = models.OneToOneField(
        Addsubmission, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "Partner"

        verbose_name_plural = "Partners"

    def __str__(self):
        return self.poc_fname + ' ' + self.poc_lname


class Ier(models.Model):
    information_ype = models.CharField('Information Type', max_length=5000, choices=[('', 'Information Type'), ('chat', 'chat'), (' chat', 'chat'), (
        'chat', 'chat'), ('chat', 'chat'), (' GPS', 'GPS'), ('GPS(IFF)', 'GPS (IFF)'), ('GPS', 'GPS'), ('GPS GPS', 'GPS GPS'), ('Sensor Data', 'Sensor Data'), ('Software Update/Patch', 'Software Update/Patch'), (' TADIL or TDL', 'TADIL or TDL'), (' Video', 'Video'), (' Voice', 'Voice'), (' Other(Please describe)', 'Other(Please describe)')])
    purpose = models.CharField('Purpose', max_length=5000)
    ion = models.CharField('Justification', max_length=5000)
    ops_impact = models.CharField(
        'Operational Impact if this IER is Not Met', max_length=5000)
    information_type = models.CharField('Information Type', max_length=5000)
    fore_m = models.CharField(
        'F (FMS CDS)', max_length=50, choices=[('', 'FMS'), (' Yes', 'Yes'), (' No', 'No'), ])
    data_format = models.CharField(
        'Data Format (If applicable)', max_length=500)
    waveform = models.CharField('Waveform(s) (If applicable)', max_length=400)
    transport_path = models.CharField('Transport Path(s)', max_length=500, choices=[('', 'Transportation Path'), ('FIBER', 'FIBER'), (
        'IP', 'IP'), ('RE (BLOS)', 'RE (BLOS)'), (' RF (LOS)', 'RF (LOS)'), (' SATCOM', 'SATCOM'), (' SERIAL', 'SERIAL'), (' OTHER', 'OTHER')])
    on_data = models.CharField(
        'ion of Data', max_length=50, choices=[('', 'ion Of Data'), ('CLASS', 'CLASS'), (' CLASS', 'CLASS'), (' CLASS', 'CLASS'), (' OTHER', 'OTHER'),])
    release = models.CharField('Releasability', max_length=500, choices=[('', 'Releasability'), (
        'Bi-Lateral (US and PN)', 'Bi-Lateral (US and PN)'), ('Multi-Lateral', 'Multi-Lateral')])
    frequency = models.CharField('Frequency', max_length=500, choices=[('', 'Frequency'), ('Event Driven', 'Event Driven'), (
        'Continuous', 'Continuous'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annually', 'Annually')])
    duration = models.CharField('Duration', max_length=500, choices=[('', 'Duration'), ('Continuous', 'Continuous'), (
        'Exercise', 'Exercise'), ('Event Driven', 'Event Driven'), ('Specified End Date(s)', 'Specified End Date(s)')])

    reference = models.CharField('Reference(s)', max_length=500)
    # upload = models.FileField('Upload', max_length=500)
    additional_information = models.CharField(
        'Additional Information', max_length=500)
    submission = models.OneToOneField(
        Addsubmission, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "Ier"

        verbose_name_plural = "Iers"

    def __str__(self):
        return self.information_ype


class Userinformations(models.Model):
    platform_type = models.CharField('Platform Type', max_length=500, choices=[('', 'Platform Type'), (
        'Air', 'Air'), ('Ground (Mobile)', 'Ground (Mobile)'), ('Ground (Stationary)', 'Ground (Stationary)'), ('Marine', 'Marine'), ('Space', 'Space'), ('Sea', 'Sea'), ('J8', 'J8'), ('More than one', 'More than one')])
    capability_name = models.CharField('Capibility Name', max_length=500)
    sender_node = models.CharField('Sender Node(s)', max_length=500)
    receiver_node = models.CharField('Receiver Node(s)', max_length=500)
    intermediate_node = models.CharField('Intermediate Node', max_length=500)
    architecture_ov1 = models.CharField('Architecture OV1', max_length=500)
    equipment_information = models.CharField(
        'Equipment Information', max_length=500)
    general_location = models.CharField('AOR/General Location', max_length=500)
    cross_cocom = models.CharField(
        'Cross-COCOM', max_length=100, choices=[('', 'Cross COCOM'), ('Yes', 'Yes'), ('No', 'No'), ('Other', 'Other')])
    position = models.CharField('Position', max_length=100)
    organization = models.CharField('Organization', max_length=200)
    da_te = models.DateField(auto_now=True)
    submission = models.OneToOneField(
        Addsubmission, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "Userinformation"

        verbose_name_plural = "Userinformations"

    def __str__(self):
        return self.platform_type


class Signaturecentcom(models.Model):
    name = models.CharField('Name', max_length=500)
    position = models.CharField('Position', max_length=100)
    organization = models.CharField('Organization', max_length=100)
    # date = models.DateTimeField()
    submission = models.OneToOneField(
        Addsubmission, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "Signaturecentcom"

        verbose_name_plural = "Signaturecentcoms"

    def __str__(self):
        return self.name


class Signaturepartner(models.Model):
    name = models.CharField('Name', max_length=500)
    position = models.CharField('Position', max_length=100)
    organization = models.CharField('Organization', max_length=100)
    # date = models.DateTimeField(auto_now=True)
    submission = models.OneToOneField(
        Addsubmission, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Signaturepartner"

        verbose_name_plural = "Signaturepartner"

    def __str__(self):
        return self.name
