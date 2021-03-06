# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-30 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duminfo', '0003_auto_20181116_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='dumuser',
            name='AdDebt',
            field=models.CharField(help_text='Debts & other liabilities incurred by him/her directly or indirectly', max_length=200, null=True, verbose_name='Debts and Liabilitiess'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='AddrLine1',
            field=models.CharField(max_length=100, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='AddrLine2',
            field=models.CharField(max_length=100, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='AddrLine3',
            field=models.CharField(max_length=100, null=True, verbose_name='Address Line 3'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='AsMov',
            field=models.CharField(help_text='Other movable property inherited by him/her or similarly owned acquired or held by him/her', max_length=200, null=True, verbose_name='Movable Assets Details'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='AsShares',
            field=models.CharField(help_text='Shares, Debentures and Cash, including bank deposits inherited by him/her or similarly acquired or held by him/her', max_length=200, null=True, verbose_name='Shares Details'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='Dadnat',
            field=models.CharField(max_length=10, null=True, verbose_name='Father Nationality'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='EmpNo',
            field=models.CharField(help_text='Employee number or Roll Number', max_length=20, null=True, verbose_name='Unique ID'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='FName',
            field=models.CharField(max_length=20, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='HadLn1',
            field=models.CharField(help_text='House Number, Land/Street/Road', max_length=100, null=True, verbose_name='Home Address Line 1'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='HadLn2',
            field=models.CharField(max_length=100, null=True, verbose_name='Home Address Line 2'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='HadLn3',
            field=models.CharField(help_text='Village, Thana and District', max_length=100, null=True, verbose_name='Home Address Line 3'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='JustifOsSw',
            field=models.CharField(max_length=100, null=True, verbose_name='If requered OS/SW Justification'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='LName',
            field=models.CharField(max_length=20, null=True, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='MomAddr',
            field=models.CharField(help_text='Present address (if dead give last address)', max_length=25, null=True, verbose_name='Mother Address'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='MomDesigAddr',
            field=models.CharField(help_text='Occupation(if employed give designation  &  official address)', max_length=25, null=True, verbose_name='Mother Occupation'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='MomPermAddr',
            field=models.CharField(max_length=25, null=True, verbose_name='Mother Permanant Address'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='Momnat',
            field=models.CharField(max_length=10, null=True, verbose_name='Mother Nationality'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='Natlty',
            field=models.CharField(max_length=25, null=True, verbose_name='Your Nationality'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='PakAdL1',
            field=models.CharField(help_text='If originally a resident of Pakistan, the address in that Country and the date of migration to Indian Union.', max_length=100, null=True, verbose_name='Pakisthan Adddress if Any line 1'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='PakAdL2',
            field=models.CharField(max_length=100, null=True, verbose_name='Pakisthan Adddress 2'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='PakAdL3',
            field=models.CharField(help_text='Village, Thana and District', max_length=100, null=True, verbose_name='Pakisthan Adddress if Any line 13'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='ProxyReq',
            field=models.CharField(help_text='yes with reason or No', max_length=100, null=True, verbose_name='Account on Proxy Server for Internet Connectivity '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='ScSt',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Are you a member of a Scheduled Caste/ Scheduled Tribe ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='SpoAddr',
            field=models.CharField(help_text='Present address (if dead give last address)', max_length=25, null=True, verbose_name='Spouse Address'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='SpoDesigAddr',
            field=models.CharField(help_text='Occupation(if employed give designation  &  official address)', max_length=25, null=True, verbose_name='Spouse Occupation'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='SpoNam',
            field=models.CharField(max_length=20, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='SpoPermAddr',
            field=models.CharField(max_length=25, null=True, verbose_name='Spouse Permanant Address'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='Sponat',
            field=models.CharField(max_length=10, null=True, verbose_name='Spouse Nationality'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='TodayDate',
            field=models.DateField(null=True, verbose_name='Time of Joining '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='age',
            field=models.CharField(max_length=10, null=True, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='arrested',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Have you ever been arrested ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='banKAcNo',
            field=models.CharField(max_length=25, null=True, verbose_name='Bank Account Number '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='birthPlace',
            field=models.CharField(max_length=10, null=True, verbose_name='BirthPlace'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='birthdistrict',
            field=models.CharField(max_length=10, null=True, verbose_name='Birth District'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='boundDown',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Have you ever been bound down ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='clsXage',
            field=models.CharField(max_length=10, null=True, verbose_name='Age at Matriculation (Standard X)'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='convicted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Have you ever been convicted by a court of law for any offence ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='crimeDesc',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', help_text='If the answer to any of above mentioned question is ‘Yes’, give full particulars of the case / arrest/ detention/ fine/ conviction/ sentence/ punishment etc. and / or the nature of the case pending in the Court/ University/ Education Authority etc., at time of filling up this form', max_length=4, null=True, verbose_name='Description of Above'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dadAddr',
            field=models.CharField(help_text='Present address (if dead give last address)', max_length=25, null=True, verbose_name='Father Address'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dadDesigAddr',
            field=models.CharField(help_text='Occupation(if employed give designation  &  official address)', max_length=25, null=True, verbose_name='Father Occupation'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dadNam',
            field=models.CharField(max_length=20, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dadPermAddr',
            field=models.CharField(max_length=25, null=True, verbose_name='Father Permanant Address'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dateOfJoin',
            field=models.DateField(null=True, verbose_name='Date of Joining '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='debarUniv',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', help_text=' from any examination or rusticated by any University or any other educational authority / Institution ?', max_length=4, null=True, verbose_name='Have you ever been debarred From University '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='debatPubSer',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', help_text='isqualified by any Public Service Commission from appearing at its examination / selection', max_length=4, null=True, verbose_name='Have you ever been debarred From Examinations ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dept',
            field=models.CharField(help_text='dept/center/section', max_length=20, null=True, verbose_name='Department '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='detention',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Have you ever been kept under detention ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dummyChar1',
            field=models.CharField(help_text='Without Domain Name', max_length=20, null=True, verbose_name='Desired Email Id option 1: '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dummyChar2',
            field=models.CharField(max_length=20, null=True, verbose_name='Desired Email Id option 2: '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='dummyChar3',
            field=models.CharField(max_length=20, null=True, verbose_name='Desired Email Id option 3: '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='fatherDistrict',
            field=models.CharField(help_text=' District and State to which your father      originally belongs', max_length=10, null=True, verbose_name='District of Father'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='fined',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Have you ever been fined by a court of law ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='fullName',
            field=models.CharField(help_text='the full name of the person Filling the form', max_length=40, null=True, verbose_name='Full Name'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='localityRef1',
            field=models.CharField(help_text='Name of two responsible persons of your locality or two references to whom you are known.', max_length=25, null=True, verbose_name='Reference 1'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='localityRef2',
            field=models.CharField(max_length=25, null=True, verbose_name='Reference 1'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='momNam',
            field=models.CharField(max_length=20, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='pbDad',
            field=models.CharField(max_length=10, null=True, verbose_name='Father Place of Birth'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='pbMom',
            field=models.CharField(max_length=10, null=True, verbose_name='Mother Place of Birth'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='pbSpof',
            field=models.CharField(max_length=10, null=True, verbose_name='Spouse Place of Birth'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='pcRec',
            field=models.CharField(help_text='yes Or No', max_length=100, null=True, verbose_name='PC Requisition '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='pendCourt',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', help_text='or any other educational authority/ institution ', max_length=4, null=True, verbose_name='Is any case pending against you in any court of law ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='pendUniv',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Is any case pending against you in any University ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='place',
            field=models.CharField(max_length=25, null=True, verbose_name='Place '),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='post',
            field=models.CharField(max_length=20, null=True, verbose_name='Current Post'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='prosecuted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4, null=True, verbose_name='Have you ever been prosecuted ?'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='relDate',
            field=models.DateField(null=True, verbose_name='Relieving order Date'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='relievingOrNo',
            field=models.CharField(help_text='Please enclose Copy', max_length=20, null=True, verbose_name='Relieving order no'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='religion',
            field=models.CharField(max_length=15, null=True, verbose_name='Religion'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='remarks',
            field=models.CharField(max_length=200, null=True, verbose_name='Remarks (if Any)'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='scstName',
            field=models.CharField(max_length=25, null=True, verbose_name='if the answer is ‘Yes’, state the name threof.'),
        ),
        migrations.AddField(
            model_name='dumuser',
            name='timeOfJoin',
            field=models.CharField(max_length=20, null=True, verbose_name='Time of Joining'),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='f1',
            field=models.CharField(help_text='Unique identifier for the student s', max_length=100, null=True, verbose_name='Ful Nam (Recheck)'),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='f2',
            field=models.CharField(max_length=20, null=True, verbose_name=''),
        ),
    ]
