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

        verbose_name_plural = "Addsubmission"

    def __str__(self):
        return self.fname + ' ' + self.lname


class Intell(models.Model):
    product = models.CharField('Product', max_length=250, choices=[('', 'Product'), ('Commander Daily Update (CDU)', 'Commander Daily Update (CDU)'), ('Joint Collection Management Board Update (JCMB)', 'Joint COllection Mnagement Board Update (JCMB)'), (
        'High Value Detainee Report(HVD)', 'High Value Detainee Report (HVD)'), ('Daily Intelligence Summary (DISUM)', 'DAILY Intelligence Summary (DISUM)'), ('Daily Intelligence Cables', 'Daily Intelligence Cables'), ('J2 LNO Reports', 'J2 LNO Reports'), ('First Look Input', 'First Look Input'), ('SECDEF Sitrep', 'SECDEF Sitrep'), ('CSAR/CSEL', 'CSAR/CSEL'), ('Counter IED', 'Counter IED'), ('Intelligence Articles', 'Intelligence Articles'), ('ISR Highlights', 'ISR Highlight'), ('Monthly Allocation Directive (MAD)', 'Month Allocation Directive (MAD)'), ('Warning Issue Reports/Advisories', 'Warning Reports/Advisories'), ('Threat Assessments', 'Threat Assessments'), ('VIP Briefing', 'VIP Briefing'), ('Information Papers', 'Information Papers'), ('Desk Notes', 'Desk Notes'), ('JICCENT Special Reports (JSR)', 'JICCENT Special Reports(JSR)'), ('Defense Readiness Report System Update (DRRS)', 'Defense Readiness Report System Update (DRRS)'), ('Joint Forces Readiness Report Assessment (JFRR/DRRS)', 'Joint Forces Readiness Report Assessment (JFRR/DRRS)'), ('JS J2 & Cos Update', 'JS J2 & Cos Update'), ('J2-P Update', 'J2-P Update'), ('Intel Ops Synchronization Meeting (IOSM)', 'Intel Ops Synchronization Meeting (IOSM)'), ('Critical Plan Updates', 'Critical Plan Updates'), ('Intelligence Readbook', 'Intelligence Readbook'), ('JCS J2 VTC', 'JCS J2 VTC'), ('SNR Brief', 'SNR Brief'), ('Leadership Notification', 'Leadership Notification'), ('Global SIGINT Highlights (GSH)', 'Global SIGINT Highlight (GSH)'), ('JICCENT Intel Notes, Memos, Vessel of Interest Reports, Tripbook', 'JICCENT Intel Notes, Memos, Vessels of Interest Reports, Tripbook'), ('OSINT Tracker', 'OSINT Tracker'), ('Executive Joint Collection Management Board (EJCMB)', 'Executive Joint Collection Management Board (EJCMB)'), ('SPECAT JCMB', 'SPECAT JCMB'), ('Joint Explotation Management Board', 'Joint Explotation Management Board'), ('ISR Improvement VTC', 'ISR Improvement VTC'), ('Collection Focus Area Slides', 'Collection Focus Area SLides'), ('HUMINT Requirements, IIR Evaluations', 'HUMINT Requirements, IIR Evaluations'), ('HUMINT Assessment Brief', 'HUMINT Assessment Brief')])

    rational = models.CharField(max_length=2500, choices=[('', 'Rational'), ('Force Protection', 'Force Protection'), ('SA', 'SA'), ('ISR Priorities; Collection Integration and Synchronization', 'Collection Integration and Synchronization'), ('SA Intel Ops Coordination', 'SA Intel Ops Coordination'), ('Support CAG SECDEF Report', 'Support CAG SECDEF Report'), ('Lesson Learned', 'Lesson Learned'), (
        'Force Protection/SA', 'Force Protection/SA'), ('SA Response to Questions', 'SA Response to Questions'), ('JS Requirement', 'JS Requirement'), ('JS and Cos Requirement', 'JS and Cos Requirement'), ('J2 Important Information', 'J2 Important Information'), ('J2 Needed Information', 'J2 Needed Information'), ('SA w/COCOMs', 'SA W/COCOMs'), ('CDR Requirement', 'CDR Requirement'), ('Warning SA', 'Warning SA'), ('SA Response to question, Support CDR for Travel', 'SA Response to question, Support CDR for Travel'), ('ISR Priorities Decison Making, Guidance and Objectives, Apportionment and Allocation', 'ISR Priorities Decision Making, Guidance and Objectives, Appointment and Allocation'), ('Special Collection Requirements and Operations', 'Special Collection Requirements and Operations'), ('PED Capacity and Execution', 'PED Capacity and Execution'), ('Lesson Learned and New Capabilities', 'Lesson Learned and New Capabilities'), ('Requirements, Integration and Synchronization', 'Requirements, Integration and Synchronization'), ('Coordination and Consumer Feedback', 'Coordination and Consumer Feedback'), ('Quantative HUMINT Assessment base on PIRs, ISR Priorities and basic IFC Topics ', 'Quantative HUMINT Assessment base on PIRs, ISR Priorities and basic IFC Topics')])

    frequency = models.CharField('Frequency', max_length=2500, choices=[('', 'Frequency'), ('Daily', 'Daily'), (
        'Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('As Required', 'As Required'), ('Bimonthly', 'Bimonthly'), ('By Event', 'By Event')])

    format = models.CharField(max_length=2500, choices=[(
        '', 'Format'), ('Data, Voices, Text', 'Data, Voice, Text'), ('Text / Graphical Display', 'Text / Graphical Display'), ('Text', 'Text'), ('HTML', 'HTML'), ('Text, Voice', 'Text, Voice'), ('Data, Text', 'Data, Text')])

    sourcesofinput = models.CharField(
        max_length=2500, choices=[('', 'Source Of Input'), ('Intel Reporting', 'Intel Reporting'), ('Task Forces, Components, J3-OR, J2-O/P/R/X, JIC', 'Task Forces Compoments, J3-OR, J2-O/P/R/X'), ('OIF HUMINT', 'OIF HUMINT'), ('Ops Report', 'Ops Report'), ('Unit/Intel Reporting', 'Unit /Intel Reporting'), ('Unit Reporting', 'Unit Reporting'), ('Collections Reporting', 'Collections Reporting'), ('NSA', 'NSA'), ('Open Source Reporting', 'Open Source Reporting'), ('Task Forces and Compo-nents, J3-OR, J2-O, J2-P, J2-R, J2-X, JICCENT', 'Task Forces and Compo-nents, J3-OR, J2-O, J2-P, J2-R, J2-X, JICCENT'), ('Federated Exploitation Enterprise, 480 IW, 513 MI BDE', 'Federated Exploitation Enterprise, 480 IW, 513 MI BDE'), ('Task Forces, Components, J3-OR, J2-O, J2-P, J2-R, J2-X, JICCENT, Combat Support Agencies', 'Task Forces, Components, J3-OR, J2-O, J2-P, J2-R, J2-X, JICCENT, Combat Support Agencies'), ('JICCENT Analysts, IC Analysts ', 'JICCENT Analysts, IC Analysts '), ('Message Traffic IIRs citing HUMINT Requirements and Analyst driven IIR Evaluations', 'Message Traffic IIRs citing HUMINT Requirements and Analyst driven IIR Evaluations ')])

    meansofinfo = models.CharField(max_length=2500, choices=[('', 'Means Information is Extracted'), ('IBS, Secure Phone', 'IBS, Secure Phone'), ('M3, Pathfinder, WebTAS, websites, email, databases', 'M3, Pathfinder, WebTAS, websites, email, databases'), ('Meetings, VTCs, databases, websites, email', 'Meetings, VTCs, databases, websites, email'), ('HDWS, Databases, M3, BATS, websites', 'HDWS, Databases, M3, BATS, websites'), ('M3, Email', 'M3, Email'), ('SIPR Email', 'SIPR Email'), ('M3, Secure Phone, Email', 'M3, Secure Phone, Email'), (
        'AMHS, Secure Phone, Email', 'AMHS, Secure Phone, Email'), ('M3, Pathfinder, WebTAS, websites, email, databases, Secure Phone', 'M3, Pathfinder, WebTAS, websites, email, databases, Secure Phone'), ('Secure Phone, Email', 'Secure Phone, Email'), ('Posted to web portal or e-mail', 'Posted to web portal or e-mail'), ('Email Channels, Message Traffic, HOTR, CIDNE ', 'Email Channels, Message Traffic, HOTR, CIDNE'), ('Message Traffic, Access Database used by ISRC-HUMINT Individuals, Excel spreadsheet ', 'Message Traffic, Access Database used by ISRC-HUMINT Individuals, Excel spreadsheet ')])

    dissemination = models.CharField(max_length=2500, choices=[('', 'Dissemination'), ('GCCS/ C2PC, TBMCS, CENTCOM Execution (CEN), CHAT, Secure Phone', 'GCCS/ C2PC, TBMCS, CENTCOM Execution (CEN), CHAT, Secure Phone'), ('Briefing, Email, Web, Archive', 'Briefing, Email, Web, Archive'), ('HDWS, BATS, watch list, websites', 'HDWS, BATS, watch list, websites'), ('Web, Readbook', 'Web, Readbook'), ('Web, CCJ3’s Ops/Intel Update', 'Web, CCJ3’s Ops/Intel Update'), ('Commanders SECDEF Report', 'Commanders SECDEF Report'), ('COP/ TIP', 'COP/ TIP'), ('Shared database, Email, Web ', 'Shared database, Email, Web '), ('Shared database, Email', 'Shared database, Email'), ('Web', 'Web'), ('Shared database, Email, Secure Phone, Web', 'Shared database, Email, Secure Phone, Web'), ('Briefing, Shared database, Email', 'Briefing, Shared database, Email'), (
        'Email, Electronic Staff Package (ESP)', 'Email, Electronic Staff Package (ESP)'), ('Drive Folders', 'Drive Folders'), ('Hardcopy Book', 'Hardcopy Book'), ('VTC', 'VTC'), ('Briefing, Web (CENTRIXS)', 'Briefing, Web (CENTRIXS)'), ('Email/ ESP', 'Email/ ESP'), ('Brief, E-mail, Web Portal', 'Brief, E-mail, Web Portal'), ('Shared database, Web Portal, E-mail', 'Shared database, Web Portal,E-mail'), ('Email, Message Traffic, CIDNE ', 'Email, Message Traffic, CIDNE '), ('HUMINT Portal Post ', 'HUMINT Portal Post ')])

    primaryconsumer = models.CharField(max_length=2500, choices=[('', 'Primary Consumer'), ('Components & JTFs', 'Components & JTFs'), ('CDR ', 'CDR '), ('Components & JTFs, Combat Support Agencies, Other COCOMs', 'Components & JTFs, Combat Support Agencies, Other COCOMs'), ('National Agencies, Components & JTFs', 'National Agencies, Components & JTFs'), (
        'CDR, National Agencies, Components & JTFs', 'CDR, National Agencies, Components & JTFs'), ('J2 CDR and Staff', 'J2 CDR and Staff'), ('Commander, SECDEF', 'Commander, SECDEF'), ('DoD, Coalition, Other Agencies', 'DoD, Coalition, Other Agencies'), ('CENTCOM Joint Staff', 'CENTCOM Joint Staff'), ('CoS, CDR, J2', 'CoS, CDR, J2'), ('J2', 'J2'), ('CDR and Directors', 'CDR and Directors'), ('CCJ2 and JCS J2', 'CCJ2 and JCS J2'), ('Coalition Senior National Reps', 'Coalition Senior National Reps'), ('Commander, Staff & Components', 'Commander, Staff & Components'), ('Flag Officers, General Officers, and Senior Leaders', 'Flag Officers, General Officers, and Senior Leaders'), ('Task Forces and Select Components', 'Task Forces and Select Components'), ('PED Enterprise', 'PED Enterprise'), ('Task Forces, Components, Combat Support Agencies, and other COCOMs', 'Task Forces, Components, Combat Support Agencies, and other COCOMs'), ('J2, J3', 'J2, J3'), ('HUMINT Collectors', 'HUMINT Collectors '), ('ISRC', 'ISRC')])

    secondaryconsumer = models.CharField(max_length=2500, choices=[('', 'Secondary Consumer'), ('DoD and IC', 'DoD and IC'), ('Others, Components, JTFs & Coalition Forces', 'Others, Components, JTFs & Coalition Forces'), ('CDR, IC', 'CDR, IC'), ('IC', 'IC'), (
        'JIC', 'JIC'), ('Staff', 'Staff'), ('Coalition, Others in IC', 'Coalition, Others in IC'), ('J2 Staff', 'J2 Staff'), ('National Agencies, Components & JTFs', 'National Agencies, Components & JTFs'), ('Task Forces, Components, and Combat Support Agencies', 'Task Forces, Components, and Combat Support Agencies'), ('Select Components and Combat Support Agencies', 'Select Components and Combat Support Agencies'), ('Task Forces, Components, Combat Support Agencies, and other COCOMs', 'Task Forces, Components, Combat Support Agencies, and other COCOMs'), ('Program Offices and Intel Community', 'Program Offices and Intel Community'), ('Senior Leaders', 'Senior Leaders'), ('Collection Managers ', 'Collection Managers '), ('HUMINT Collection Managers, HSE, Analysts ', 'HUMINT Collection Managers, HSE, Analysts ')])

    produceropr = models.CharField(max_length=2500, choices=[('', 'Producer OPR'), ('J3', 'J3'), ('J2-J, J2-X', 'J2-J, J2-X'), ('CCJ2-ISRP', 'CCJ2-ISRP'), ('J2-XH', 'J2-XH'), (
        'J2-J, J2-X', 'J2-J, J2-X'), ('J2 LNO', 'J2 LNO'), ('National Technical Means (NTM)', 'National Technical Means (NTM)'), ('NTM', 'NTM'), ('J2-ISR', 'J2-ISR'), ('J2-RF', 'J2-RF'), ('J2-P', 'J2-P'), ('J2-J', 'J2-J'), ('J2-JOW', 'J2-JOW'), ('NCR-CENT', 'NCR-CENT'), ('J2-JOWO', 'J2-JOWO'), ('CCJ2-ISR', 'CCJ2-ISR'), ('CCJ2-ISRP', 'CCJ2-ISRP'), ('HUMINT Collection Managers ', 'HUMINT Collection Managers ')])

    producerocr = models.CharField(max_length=2500, choices=[('', 'Producer OCR'), ('J2', 'J2'), ('DDI', 'DDI'), (
        'J2, J3', 'J2, J3'), ('J3', 'J3'), ('DDI, J2, J3', 'DDI, J2, J3'), ('J2-ISR', 'J2-ISR'), ('DDI, FDO', 'DDI, FDO'), ('J2, J3 Staffs', 'J2, J3 Staffs'), ('IC Wide Analysts ', 'IC Wide Analysts')])

    classification = models.CharField(max_length=120, choices=[('', 'Classification'), ('S', 'S'), ('Multiple', 'Multiple'), ('SI/ TK', 'SI/ TK'), (
        'S// REL FVEY', 'S// REL FVEY'), ('S and Below', 'S and Below'), ('SECRET// REL', 'SECRET// REL'), ('TS//SCI', 'TS//SCI'), ('Usually Collateral', 'Usually Collateral')])

    policyguidance = models.CharField(max_length=210, choices=[('', 'Policy Guidance & Directive'), (
        'CENTCOM Theater Air and Missile Defense (TAMD) CONOPS', 'CENTCOM Theater Air and Missile Defense (TAMD) CONOPS'), ('CAPCO/ DoD Instruction', 'CAPCO/ DoD Instruction'), ('JCMB CONOPS', 'JCMB CONOPS'), ('Division Chief, J2 Guidance', 'Division Chief, J2 Guidance'), ('EJCMB CONOPS', 'EJCMB CONOPS'), ('SPECAT CONOPS', 'SPECAT CONOPS'), ('JEMB CONOPS', 'JEMB CONOPS'), ('ISR Improve-ment VTC CONOPS', 'ISR Improve-ment VTC CONOPS'), ('DIAM 58-12 ', 'DIAM 58-12 ')])

    class Meta:
        verbose_name = "J2 (Intell)"
        verbose_name_plural = "J2 (Intell)"


note = models.TextField(max_length=25000)
