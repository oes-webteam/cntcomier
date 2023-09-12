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


class Strategies(models.Model):
    product = models.CharField(max_length=250, choices=[
        ('', 'Product'), ('Command Planning Board Plans Briefs and Updates', 'Command Planning Board Plans Briefs and Updates'), ('JSCP Plan IPR Briefs', 'JSCP Plan IPR Briefs'), ('Commander Directed Plan Briefings/ IPRs', 'Commander Directed Plan Briefings/ IPRs'), ('Library of Strategic Documents', 'Library of Strategic Documents'), ('Theater Strategy', 'Theater Strategy'), ('AOR Classified Brief', 'AOR Classified Brief')])

    rational = models.CharField(max_length=250, choices=[(
        '', 'Rational'), ('Obtain input, guidance, and/or approval from cross directorate planners and leadership regarding plans development', 'Obtain input, guidance, and/or approval from cross directorate planners and leadership regarding plans development'), ('Provide IPRs to Joint Staff and/or SECDEF regarding JSCP mandated plans', 'Provide IPRs to Joint Staff and/or SECDEF regarding JSCP mandated plans'), ('Provide IPRs to Command Group for input and/or approval', 'Provide IPRs to Command Group for input and/or approval'), ('Strategic Analysis Source', 'Strategic Analysis Source'), ('Strategic Planning', 'Strategic Planning'), ('Situational Awareness', 'Situational Awareness')])

    frequency = models.CharField(max_length=250, choices=[('', 'Frequency'), ('Weekly', 'Weekly'), (
        'As scheduled', 'As scheduled'), ('As scheduled, directed, or required', 'As scheduled, directed, or required'), ('As Updated', 'As Updated')])

    format = models.CharField(max_length=250, choices=[('', 'Format'), ('Electronic Briefing, power point slide', 'Electronic Briefing, power point slide'), (
        'Text, Graphics', 'Text, Graphics'), ('PPT', 'PPT')])

    sourcesofinput = models.CharField(max_length=250, choices=[(
        '', 'Sources of Input'), ('Staff planners from J5 and other directorates', 'Staff planners from J5 and other directorates'), ('Various', 'Various'), ('J5-ST and Cross Directorate', 'J5-ST and Cross Directorate')])

    means_info_extracted = models.CharField(max_length=250, choices=[(
        '', 'Means Info is extracted'), ('Planning team sessions, staff working groups', 'Planning team sessions, staff working groups'), ('CCJ5 Webpage', 'CCJ5 Webpage'), ('CCJ5 Webpage / Centcom Homepage', 'CCJ5 Webpage / Centcom Homepage'), ('CCJ5 Webpage (upon brief completion)', 'CCJ5 Webpage (upon brief completion)')])

    dissemination = models.CharField(max_length=250, choices=[('', 'Dissemination'), ('Read aheads provided to session attendees, and briefings posted on SIPRNET R Drive', 'Read aheads provided to session attendees, and briefings posted on SIPRNET R Drive'), (
        'Deskside pre-brief to principle if requested', 'Deskside pre-brief to principle if requested'), ('Posted on CCJ5 Webpage', 'Posted on CCJ5 Webpage'), ('Brief', 'Brief')])

    primaryconsumer = models.CharField(
        max_length=250, choices=[('', 'Primary Consumer'), ('Planners and leadership from directorates up to the Command Group', 'Planners and leadership from directorates up to the Command Group'), ('SECDEF, Joint Staff, CENTCOM CDR', 'SECDEF, Joint Staff, CENTCOM CDR'), ('Commander, DCOM, or COS', 'Commander, DCOM, or COS'), ('CENTCOM Components', 'CENTCOM Components'), ('CENTCOM Visitors', 'CENTCOM Visitors')])

    secondaryconsumer = models.CharField(max_length=250, choices=[(
        '', 'Secondary Consumer'), ('Staff Coalition and LNO Planners', 'Staff Coalition and LNO Planners'), ('Internal Planners', 'Internal Planners'), ('Others Components, Staff, JS, OSD', 'Others Components, Staff, JS, OSD'), ('CENTCOM Components, Others Components, Staff, JS, OSD', 'CENTCOM Components, Others Components, Staff, JS, OSD')])

    produceropr = models.CharField(max_length=250, choices=[
        ('', 'Producer OPR'), ('J5-P', 'J5-P'), ('J5-P or J3-P in support of CDR/ DCOM', 'J5-P or J3-P in support of CDR/ DCOM'), ('J5-P or J3-P', 'J5-P or J3-P'), ('Various', 'Various'), ('CENTCOM', 'CENTCOM'), ('CCJ5-ST', 'CCJ5-ST')])

    producerocr = models.CharField(max_length=250, choices=[
        ('', 'Producer OCR'), ('Various', 'Various'), ('CCJ1-8', 'CCJ1-8')])

    classification = models.CharField(max_length=250, choices=[(
        '', 'Classification'), ('SECRET REL up to TS//NOFORN', 'SECRET REL up to TS//NOFORN'), ('S and Unclass', 'S and Unclass'), ('S', 'S')])

    policy_guidance_directive = models.CharField(
        max_length=250, choices=[('', 'Policy Guidance / Directive'), ('Command Planning Board Charter (Draft in staffing)', 'Command Planning Board Charter (Draft in staffing)'), ('JSCP Guidance', 'JSCP Guidance'), ('Theater Campaign Plan, CDR/ DCOM Guidance', 'Theater Campaign Plan, CDR/ DCOM Guidance'), ('Various', 'Various')])

    note = models.TextField(max_length=25000)
