from django.db import models
# Create your models here.


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


class Logistic(models.Model):
    product = models.CharField(max_length=250, choices=[('', 'Product'), ('Engineer SITREP', 'Engineer SITREP'), ('MPL & CPL submissions', 'MPL & CPL submissions'), ('OEF/OIF Air Munitions Expenditure', 'OEF/OIF Air Munitions Expenditure'), (
        'Ground Ammunition Status ', 'Ground Ammunition Status'), ('AOR Fuel Supply Status  ', 'AOR Fuel Supply Status'), ('Mortuary Affairs', 'Mortuary Affairs'), ('Contractor Census', 'Contractor Census'), ('Daily Update Report', 'Daily Update Report')])

    rational = models.CharField(max_length=250, choices=[('', 'Rational'), ('Situational Awareness', 'Situational Awareness'), (
        'SA, JS requirement', 'SA, JS requirement'), ('SA', 'SA')])

    frequency = models.CharField(max_length=250, choices=[('', 'Frequency'), ('Ea FRI', 'Ea FRI'), (
        'As Directed', 'As Directed'), ('Daily', 'Daily'), ('Quarterly', 'Quarterly')])

    format = models.CharField(max_length=250, choices=[('', 'Format'), ('Text, Excel', 'Text, Excel'), (
        'Text, Excel', 'Text, Excel'), ('Text', 'Text'), ('Text/Powerpoint', 'Text/Powerpoint'), ('Excel via email and internet', 'Excel via email and internet')])

    sourcesofinput = models.CharField(max_length=250, choices=[('', 'Sources of Input'), (
        'Components, JTFs', 'Components, JTFs'), ('CFACC, CFMCC', 'CFACC, CFMCC'), ('Joint Mortuary Affairs (Services)', 'Joint Mortuary Affairs (Services)'), ('Service Components and Services', 'Service Components and Services'), ('CJTF-101, MNC-I, CFLCC, CFACC, CFMCC, DESC-ME SITREP, Truck Report', 'CJTF-101, MNC-I, CFLCC, CFACC, CFMCC, DESC-ME SITREP, Truck Report')])

    meansinfoextracted = models.CharField(max_length=250, choices=[('', 'Means Info is extracted'), ('Submitted Reports', 'Submitted Reports'), ('EMAILS, WEB PAGE', 'EMAILS, WEB PAGE'), (
        'Web-based/excel REPOL & DESC reports', 'Web-based/excel REPOL & DESC reports'), ('Manual', 'Manual '), ('Electronic via internet and email', 'Electronic via internet and email')])

    dissemination = models.CharField(max_length=250, choices=[('', 'Dissemination'), ('Email', 'Email'), ('Web Page, Joint Total Access Visibility (JTAV)', 'Web Page, Joint Total Access Visibility (JTAV)'), (
        'Email,  Web page, AMHS', 'Email,  Web page, AMHS'), ('Email, Web page', 'Email, Web page'), ('Web page ', 'Web page'), ('OSD, Joint Staff', 'OSD, Joint Staff'), ('Via email, CENTCOM webpage.', 'Via email, CENTCOM webpage.')])

    primaryconsumer = models.CharField(max_length=250, choices=[(
        '', 'Primary Consumer'), ('CENTCOM', 'CENTCOM'), ('JS, CCJ4-O', 'JS, CCJ4-O'), ('CCJ4-O', 'CCJ4-O'), ('CCJ4-C', 'CCJ4-C'), ('CDR', 'CDR')])

    secondaryconsumer = models.CharField(max_length=250, choices=[(
        '', 'Secondary Consumers'), ('N/A', 'N/A'), ('OSD, Service Components', 'OSD, Service Components'), ('J4 DIRECTOR/DEP DIRECTOR, J3 DIRECTOR/DEP DIRECTOR, J3-O-CAS , J4-O, JCS SJS, JCS J4/SD', 'J4 DIRECTOR / DEP DIRECTOR, J3 DIRECTOR/DEP DIRECTOR, J3-O-CAS , J4-O, JCS SJS, JCS J4/SD'), ('ARCENT, TRANSCOM, DESC, 1st TSC, CDDOC, DLA, JCS, EUCOM JPO, TACC, AFPET, AALOCSM, MNC-I, 101st SBDE, MNF-I, CJTF-101, 165th QM GP, 311th ESC, 3rd ESC, 16th SB, HQDA', 'ARCENT, TRANSCOM, DESC, 1st TSC, CDDOC, DLA, JCS, EUCOM JPO, TACC, AFPET, AALOCSM, MNC-I, 101st SBDE, MNF-I, CJTF-101, 165th QM GP, 311th ESC, 3rd ESC, 16th SB, HQDA'), ('OSD', 'OSD'), ('Others Components, Staff, JS, OSD', 'Others Components, Staff, JS, OSD')])

    produceropr = models.CharField(
        max_length=250, choices=[('', 'Producer OPR'), ('CCJ4-E', 'CCJ4-E'), ('Components, JTFs', 'Components, JTFs'), ('Service Components', 'Service Components'), ('CCJ4-OJMO', 'CCJ4-OJMO'), ('CCJ4-OJPO', 'CCJ4-OJPO'), ('CCJ4-C', 'CCJ4-C')])

    producerocr = models.CharField(max_length=250, choices=[(
        '', 'Producer OCR'), ('N/A', 'N/A'), ('DESC, MNC-I, AFCENT, CJTF-101, 311th ESC, 165th QM GP', 'DESC, MNC-I, AFCENT, CJTF-101, 311th ESC, 165th QM GP'), ('Service Components and Services', 'Service Components and Services')])

    classification = models.CharField(
        max_length=250, choices=[('', 'Classification'), ('S/Rel ', 'S/Rel '), ('FOUO', 'FOUO'), ('Unclass', 'Unclass'), ('Secret', 'Secret')])

    policy_guidance_directive = models.CharField(max_length=250, choices=[('', 'Policy Guidance Directive'), (
        'CCR 415-1', 'CCR 415-1'), ('DoD Instruction US Code', 'DoD Instruction US Code'), ('MUREP REPORTING  FOR 1003V from JSJ4', 'MUREP REPORTING  FOR 1003V from JSJ4'), ('No policy, guidance, directive. Produced only as directed.', 'No policy, guidance, directive. Produced only as directed.'), ('DODI 3020.41/CENTCOM FRAGO', 'DODI 3020.41/CENTCOM FRAGO'), ('Joint Publication 4-03: Joint Bulk Petroleum and Water Doctrine.  CCJ4-JPO Local Policy', 'Joint Publication 4-03: Joint Bulk Petroleum and Water Doctrine.  CCJ4-JPO Local Policy')])

    note = models.TextField(max_length=25000)
