from django.db import models
from datetime import date

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


class Operation(models.Model):
    product = models.CharField('Product', max_length=250, choices=[('', 'Product'), ('CUB Maritime focus area', 'CUB Maritime focus area'), ('OPS and INTEL Brief Maritime update', 'OPS and INTEL Brief Maritime update'), (
        'Retrieving data. Wait a few seconds and try to cut or copy again', 'Retrieving data. Wait a few seconds and try to cut or copy again'), ('TLAM Status', 'TLAM Status'), ('Marine Expeditionary Unit (MEU) Commitment', 'Marine Expeditionary Unit (MEU) Commitment'), ('5th Fleet Scheme of Maneuver', '5th Fleet Scheme of Maneuver'), ('Coalition Scheme of Maneuver', 'Coalition Scheme of Maneuver'), ('Operational Weather Update', 'Operational Weather Update'), ('CDR Travel Weather', 'CDR Travel Weather'), ('Recon 4 Msgs', 'Recon 4 Msgs'), ('Recon 3 Msgs', 'Recon 3 Msgs'), ('Monthly Allocation Directive', 'Monthly Allocation Directive'), ('Air Order of Battle', 'Air Order of Battle'), ('Daily Boardwalk Brief', 'Daily Boardwalk Brief'), ('Daily ATO Strike Summary', 'Daily ATO Strike Summary'), ('Monthly ATO Strike Summary', 'Monthly ATO Strike Summary'), ('SNR Weekly Strike Rollup', 'SNR Weekly Strike Rollup'), ('SNR Monthly Strike Rollup', 'SNR Monthly Strike Rollup'), ('CENTCOM SITREP', 'CENTCOM SITREP'), ('ATO Weekly Sortie Summary', 'ATO Weekly Sortie Summary'), ('HOA/OEF/OIF Monthly Sortie Summary', 'HOA/OEF/OIF Monthly Sortie Summary'), ('CUB CAS (AFG) focus area', 'OPS and INTEL Brief CAS (AFG) update'), ('SNR (AFG) focus area', 'SNR (AFG) focus area'), ('Component Commaders Brief', 'Component Commaders Brief'), ('CUB AP (IRQ) focus area', 'CUB AP (IRQ) focus area'), ('OPS and INTEL Brief AP (IRQ) update', 'OPS and INTEL Brief AP (IRQ) update'), ('SNR (IRQ) focus area', 'SNR (IRQ) focus area'), ('Component Commaders Brief', 'Component Commaders Brief')])

    rational = models.CharField(max_length=2500, choices=[('', 'Rational'), ('SA', 'SA'), ('ISR mission tracking', 'ISR mission tracking'), (
        'ISR requirements tracking', 'ISR requirements tracking'), ('Situational Awareness', 'Situational Awareness')])

    frequency = models.CharField('Frequency', max_length=2500, choices=[('', 'Frequency'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), (
        'As Required', 'As Required'), ('Bimonthly', 'Bimonthly'), ('By Event', 'By Event'), ('As Reqd', 'As Reqd'), ('Situational', 'Situational')])

    format = models.CharField(max_length=2500, choices=[(
        '', 'Format'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), ('PPT/text to First Look', 'PPT/text to First Look'), ('Text to First Look', 'Text to First Look'), ('Msg Format', 'Msg Format'), ('Excel', 'Excel'), ('High', 'High')])

    sourcesofinput = models.CharField(
        max_length=2500, choices=[('', 'Source Of Input'), ('NAVCENT', 'NAVCENT'), ('CFMCC NAVCENT', 'CFMCC NAVCENT'), ('NAVCENT MARCENT CFLCC', 'NAVCENT MARCENT CFLCC'), ('J3-OW', 'J3-OW'), ('E-mail/ Websked/ ROME', 'E-mail/ Websked/ ROME'), ('E-mail/ Tasker-Tool', 'E-mail/ Tasker-Tool'), ('.ppt product', '.ppt product'), ('Message', 'Message'), ('Excel product', 'Excel product'), ('ISAF / USFOR-A', 'ISAF / USFOR-A'), ('MNF-I & MND websites/ ISAF / USFOR-A', 'MNF-I & MND websites/ ISAF / USFOR-A')])

    meansofinfo = models.CharField(max_length=2500, choices=[('', 'Means Information is Extracted'), ('Web page', 'Web page'), ('Email Web page', 'Email Web page'), ('Joint Operations Area Forecast', 'Joint Operations Area Forecast'), (
        'Operational Weather Websites', 'Operational Weather Websites'), ('E-mail/ Websked/ ROME', 'E-mail/ Websked/ ROME'), ('E-mail/ Tasker-Tool', 'E-mail/ Tasker-Tool'), ('CFACC, MNF-I, NAVCENT, MARCENT', 'CFACC, MNF-I, NAVCENT, MARCENT'), ('AUAB CAOC', 'AUAB CAOC'), ('CFACC, NAVCENT', 'CFACC, NAVCENT'), ('AUAB CAOC', 'AUAB CAOC'), ('Numerous', 'Numerous'), ('PP submission via Email ', 'PP submission via Email '), ('Email, Web page, CIDNE', 'Email, Web page, CIDNE')])

    dissemination = models.CharField(max_length=2500, choices=[('', 'Dissemination'), ('Briefing, Email, Posted on the Web, Archive', 'Briefing, Email, Posted on the Web, Archive'), ('Briefing/Input to CHOPS First Look', 'Briefing/Input to CHOPS First Look'), ('Input to CHOPS First Look', 'Input to CHOPS First Look'), ('JS', 'JS'), ('CCJ3, Components', 'CCJ3, Components'), (
        'E-mail, Portal', 'E-mail, Portal'), ('E-mail', 'E-mail')])

    primaryconsumer = models.CharField(max_length=2500, choices=[('', 'Primary Consumer'), (
        'CDR ', 'CDR '), ('J3/J2', 'J3/J2'), ('CCC', 'CCC'), ('J3', 'J3'), ('Components', 'Components'), ('Text, Graphics', 'Text, Graphics')])

    secondaryconsumer = models.CharField(max_length=2500, choices=[('', 'Secondary Consumer'), ('J3/J2', 'J3/J2'), ('JOC', 'JOC'), ('N/A', 'N/A'), (
        'Theater METOC Personnel', 'Theater METOC Personnel'), ('HQ Staff', 'HQ Staff'), ('COCOM, Joint Staff', 'COCOM, Joint Staff'), ('COCOM', 'COCOM'), ('CCJ3', 'CCJ3')])

    produceropr = models.CharField(max_length=2500, choices=[('', 'Producer OPR'), (
        'J3-O', 'J3-O'), ('NAVCENT', 'NAVCENT'), ('J3-O-ISR', 'J3-O-ISR'), ('CENTCOM, Components, JS', 'CENTCOM, Components, JS')])

    producerocr = models.CharField(max_length=2500, choices=[('', 'Product OCR'), ('J2, J5', 'J2, J5'), ('J3-O', 'J3-O'), (
        'N/A', 'N/A'), ('28th OWS, Shaw AFB', '28th OWS, Shaw AFB'), ('None', 'None'), ('Components', 'Components'), ('CAS Air Desk', 'CAS Air Desk')])

    classification = models.CharField(max_length=120, choices=[(
        '', 'Classification'), ('S/FVEY', 'S/FVEY'), ('S/NOFORN', 'S/NOFORN'), ('S/GCTF', 'S/GCTF'), ('S/GBR', 'S/GBR'), ('S/REL GCTF', 'S/REL GCTF'), ('S', 'S'), ('S/ISAF NATO', 'S/ISAF NATO')])

    policyguidance = models.CharField(max_length=210, choices=[('', 'Policy Guidance / Directive'), (
        'Local SOP', 'Local SOP'), ('CJCSI', 'CJCSI'), ('CENTCOM J3', 'CENTCOM J3'), ('S/Rel AUS, GBR', 'S/Rel AUS, GBR'), ('S/Rel ISAF, NATO', 'S/Rel ISAF, NATO'), ('S/Rel AUS, CAN, GBR', 'S/Rel AUS, CAN, GBR'), ('S/Rel ISAF, NATO', 'S/Rel ISAF, NATO'), ('S/Rel AUS, CAN, GBR', ''), ('CCJ3-JOC Battlebook ', 'CCJ3-JOC Battlebook ')])

    class Meta:
        verbose_name = "J3 (Operation)"

        verbose_name_plural = "J3 (Operation)"

    note = models.TextField(max_length=25000)
