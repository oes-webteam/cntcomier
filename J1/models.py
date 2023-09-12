from django.db import models


# HOME TABLE
class Home(models.Model):
    description = models.TextField()
    start = models.TextField()

    class Meta:
        verbose_name = "home"

        verbose_name_plural = "home"

    def __str__(self):
        return self.description

# ADDSUBMISSION TABLE


class Addsubmission(models.Model):
    fname = models.CharField('First Name', max_length=50)
    lname = models.CharField('Last Name', max_length=50)
    location = models.CharField('Location of submission', max_length=150)
    phone = models.CharField('Phone Number', max_length=25, blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    class Meta:
        verbose_name = "Addsubmission"

        verbose_name_plural = "Addsubmission"

    def __str__(self):
        return self.fname + ' ' + self.lname


class Humanresources(models.Model):
    product = models.CharField(max_length=50, choices=[(
        '', 'Product'), ('Cub, Maj  Ops Slide', 'Cub, Maj  Ops Slide'), ('Personnel strength changes - JPERSTAT', 'Personnel strength changes - JPERSTAT'), ('CENTCOM AOR Casualties Report- Active Cases ', 'CENTCOM AOR Casualties Report- Active Cases '), ('JTF Manning', 'JTF Manning')])

    rational = models.CharField(max_length=250, choices=[(
        '', 'Rational'), ('SA', 'SA'), ('Track changes in theater troop strength', 'Track changes in theater troop strength'), ('SA, Track, report trends analysis', 'SA, Track, report trends analysis'), ('S/A', 'S/A')])

    frequency = models.CharField(max_length=250, choices=[(
        '', 'Frequency'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('CENTCOM Components and JTF’s', 'CENTCOM Components and JTF’s')])

    format = models.CharField(max_length=235, choices=[
        ('', 'Format'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), ('Web page', 'Web page'), ('Web page, e-mail, PP slide', 'Web page, e-mail, PP slide'), ('Low', 'Low')])
    sourcesofinput = models.CharField(max_length=250, choices=[(
        '', 'Source Of Input'), ('MNF-I, MNSTC-I', 'MNF-I, MNSTC-I'), ('Components', 'Components'), ('CAC Kuwait, SIGACT reports, Webpage BUA', 'CAC Kuwait, SIGACT reports, Webpage BUA'), ('N/A', 'N/A')])

    meansofinfo = models.CharField(
        max_length=250, choices=[('', 'Means Info is Extracted'), ('SIGACTS Daily Reports, Updates', 'SIGACTS Daily Reports, Updates'), ('Web page, Email', 'Web page, Email'), (' Emails, SIGACTS', ' Emails, SIGACTS'), ('Monthly', 'Monthly')])

    dissemination = models.CharField(max_length=50, choices=[(
        '', 'Dissemination'), ('Briefing, Email, Posted on the Web, Archieve', 'Briefing, Email, Posted on the Web, Archieve'), ('Joint Staff, CCJ1, CDR, Components', 'Joint Staff, CCJ1, CDR, Components'), ('CCJ1, Joint Staff, CDR', 'CCJ1, Joint Staff, CDR'), ('CoS', 'CoS')])

    primaryconsumer = models.CharField(
        max_length=250, choices=[('', 'Primary Consumer'), ('CDR ', 'CDR '), ('CDR, CCJ1', 'CDR, CCJ1'), ('Text/Data', 'Text/Data')])

    secondaryconsumer = models.CharField(
        max_length=250, choices=[('', 'Secondary Consumer'), ('Others Components, Staff, JS, OSD', 'Others Components, Staff, JS, OSD'), ('Joint Staff', 'Joint Staff'), ('SIPR', 'SIPR')])

    produceropr = models.CharField(
        max_length=250, choices=[('', 'Producer OPR'), ('J3-O', 'J3-O'), ('CCJ1-XPO', 'CCJ1-XPO'), ('Email', 'Email')])

    producerocr = models.CharField(
        max_length=250, choices=[('', 'Producer OCR'), ('J2, J5', 'J2, J5'), ('J3, J5, J2', 'J3, J5, J2'), ('Power Point Slides', 'Power Point Slides')])

    classification = models.CharField(
        max_length=250, choices=[('', 'Classification'), ('S', 'S'), ('TS', 'TS'), ('U', 'U')])

    policyguidance = models.CharField(
        max_length=250, choices=[('', 'Policy Guidance / Directive'), ('IMP pg 34 IMP Appendix', 'IMP pg 34 IMP Appendix'), ('CJCSM 3150.13A ', 'CJCSM 3150.13A ')])

    class Meta:
        verbose_name = "J1 (Human Resource)"

        verbose_name_plural = "J1 (Human Resource)"

    note = models.TextField(max_length=25000)
