from django.db import models

from django.db import models

# J5 TABLE


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

        verbose_name_plural = "Addsubmission"

    def __str__(self):
        return self.fname + ' ' + self.lname


class Jseven(models.Model):
    product = models.CharField(max_length=250, choices=[
        ('', 'Product'), ('Commander Weekly Update', 'Commander Weekly Update'), ('Significant Military Exercise Breif', 'Significant Military Exercise Breif'), ('Information Papers', 'Information Papers'), ('Defense Readiness Report System (DRRS) Update', 'Defense Readiness Report System (DRRS) Update'), ('JS J7 & CoS Updates', 'JS J7 & CoS Updates')])

    rational = models.CharField(max_length=250, choices=[(
        '', 'Rational'), ('SA', 'SA'), ('JS Requirement', 'JS Requirement'), ('JS and CoS Requirement', 'JS and CoS Requirement')])

    frequency = models.CharField(max_length=250, choices=[('', 'Frequency'), ('Weekly', 'Weekly'), (
        'As Required', 'As Required'), ('Monthly', 'Monthly'), ('Daily', 'Daily')])

    format = models.CharField(max_length=250, choices=[(
        '', 'Format'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), ('Text', 'Text'), ('PPT', 'PPT')])

    sourcesofinput = models.CharField(max_length=250, choices=[(
        '', 'Sources of Input'), ('Internal Reporting', 'Internal Reporting'), ('Unit, Component, Internal Reporting', 'Unit, Component, Internal Reporting'), ('Unit Reporting', 'Unit Reporting'), ('Collections Reporting', 'Collections Reporting')])

    means_info_extracted = models.CharField(max_length=250, choices=[(
        '', 'Means Info is extracted'), ('websites, email, databases', 'websites, email, databases'), ('AMHS, Secure Phone, Email', 'AMHS, Secure Phone, Email')])

    dissemination = models.CharField(max_length=250, choices=[('', 'Dissemination'), ('Email', 'Email'), (
        'Email, Electronic Staff Package (ESP), Message', 'Email, Electronic Staff Package (ESP), Message'), ('Email, Web', 'Email, Web')])

    primaryconsumer = models.CharField(
        max_length=250, choices=[('', 'Primary Consumer'), ('CDR', 'CDR'), ('CJCS', 'CJCS'), ('CDR and Directors', 'CDR and Directors'), ('CENTCOM Joint Staff', 'CENTCOM Joint Staff'), ('J7', 'J7')])

    secondaryconsumer = models.CharField(max_length=250, choices=[(
        '', 'Secondary Consumer'), ('Others, Components, JTFs & Coalition Forces', 'Others, Components, JTFs & Coalition Forces'), ('J7 Staff', 'J7 Staff')])

    produceropr = models.CharField(max_length=250, choices=[
        ('', 'Producer OPR'), ('J7-E, J7-P, J7-T', 'J7-E, J7-P, J7-T'), ('J7-E', 'J7-E'), ('J7-TR', 'J7-TR')])

    producerocr = models.CharField(max_length=250, choices=[
                                   ('', 'Producer OCR'), ('N/A', 'N/A')])

    classification = models.CharField(max_length=250, choices=[(
        '', 'Classification'), ('SECRET REL up to TS//NOFORN', 'SECRET REL up to TS//NOFORN'), ('S and Unclass', 'S and Unclass'), ('S', 'S'), ('Multiple', 'Multiple'), ('S and Below', 'S and Below')])

    policy_guidance_directive = models.CharField(
        max_length=250, choices=[('', 'Policy Guidance / Directive'), ('N/A', 'N/A')])

    note = models.TextField(max_length=25000)
