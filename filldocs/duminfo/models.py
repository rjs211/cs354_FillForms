from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
# Create your models here.


class DumUser(models.Model):

    yesNo = (
        ('No','No'),
        ('Yes', 'Yes')
    )

    f1 = models.CharField(max_length=100,null=True,verbose_name="Ful Nam (Recheck)",help_text='Unique identifier for the student s')
    f2 = models.CharField(max_length=20,null=True,verbose_name="",help_text='')
    f3 = models.CharField(max_length=3,null=True)
    f4 = models.DateField(null=True)
    f5 = models.CharField(max_length=3, null=True)
    f6 = models.DateField(null=True)
    fullName = models.CharField(max_length=40,null=True,verbose_name="Full Name",help_text='the full name of the person Filling the form')
    dob = models.DateField(null=True)
    post = models.CharField(max_length=20,null=True,verbose_name="Current Post",help_text='')
    dept = models.CharField(max_length=40,null=True,verbose_name="Department ",help_text='dept/center/section')
    relievingOrNo = models.CharField(max_length=20,null=True,verbose_name="Relieving order no",help_text='Please enclose Copy')
    relDate = models.DateField(null=True,verbose_name="Relieving order Date",help_text='')
    AddrLine1 = models.CharField(max_length=100,null=True,verbose_name="Address Line 1",help_text='')
    AddrLine2 = models.CharField(max_length=100,null=True,verbose_name="Address Line 2",help_text='')
    AddrLine3 = models.CharField(max_length=100,null=True,verbose_name="Address Line 3",help_text='')
    dateOfJoin = models.DateField(null=True, verbose_name="Date of Joining ", help_text='')
    timeOfJoin = models.TimeField(null=True, verbose_name="Time of Joining ", help_text='')
    #models.CharField(max_length=20,null=True,verbose_name="Time of Joining",help_text='')
    TodayDate = models.DateField(null=True, verbose_name="Today Date ", help_text='',default=datetime.date.today)
    pcRec = models.CharField(max_length=100,null=True,verbose_name="PC Requisition ",help_text='yes Or No')
    JustifOsSw = models.CharField(max_length=100,null=True,verbose_name="If requered OS/SW Justification",help_text='')
    ProxyReq = models.CharField(max_length=100,null=True,verbose_name="Account on Proxy Server for Internet Connectivity ",help_text='yes with reason or No')
    dummyChar1 = models.CharField(max_length=20,null=True,verbose_name="Desired Email Id option 1: ",help_text='Without Domain Name')
    dummyChar2 = models.CharField(max_length=20,null=True,verbose_name="Desired Email Id option 2: ",help_text='')
    dummyChar3 = models.CharField(max_length=20,null=True,verbose_name="Desired Email Id option 3: ",help_text='')
    EmpNo = models.CharField(max_length=20,null=True,verbose_name="Unique ID",help_text='Employee number or Roll Number')
    AsShares = models.CharField(max_length=200,null=True,verbose_name="Shares Details",help_text='Shares, Debentures and Cash, including bank deposits inherited by him/her or similarly acquired or held by him/her')
    AsMov = models.CharField(max_length=200,null=True,verbose_name="Movable Assets Details",help_text='Other movable property inherited by him/her or similarly owned acquired or held by him/her')
    AdDebt = models.CharField(max_length=200,null=True,verbose_name="Debts and Liabilitiess",help_text='Debts & other liabilities incurred by him/her directly or indirectly')
    remarks = models.CharField(max_length=200,null=True,verbose_name="Remarks (if Any)",help_text='')
    FName = models.CharField(max_length=20,null=True,verbose_name="your First Name",help_text='')
    LName = models.CharField(max_length=20,null=True,verbose_name="your Last Name",help_text='')
    HAdLn1 = models.CharField(max_length=100,null=True,verbose_name="Home Address Line 1",help_text='House Number, Land/Street/Road')
    HAdLn2 = models.CharField(max_length=100,null=True,verbose_name="Home Address Line 2",help_text='')
    HAdLn3 = models.CharField(max_length=100,null=True,verbose_name="Home Address Line 3",help_text='Village, Thana and District')

    homea1 = models.CharField(max_length=100, null=True, verbose_name="home Address Line 1", help_text='')
    homea3 = models.CharField(max_length=100, null=True, verbose_name="home Address Line 2", help_text='')
    homea2 = models.CharField(max_length=100, null=True, verbose_name="home Address Line 3", help_text='')

    PakAdL1 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pakisthan Adddress if Any line 1",help_text='If originally a resident of Pakistan, the address in that Country and the date of migration to Indian Union.')
    PakAdL2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pakisthan Adddress 2", help_text='')
    PakAdL3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pakisthan Adddress if Any line 13",help_text='Village, Thana and District')
    dadNam = models.CharField(max_length=20,null=True,verbose_name="Father Name",help_text='')
    Dadnat = models.CharField(max_length=10,null=True,verbose_name="Father Nationality",help_text='')
    pbDad = models.CharField(max_length=10,null=True,verbose_name="Father Place of Birth",help_text='')
    dadDesigAddr  = models.CharField(max_length=25,null=True,verbose_name="Father Occupation",help_text='Occupation(if employed give designation  &  official address)')
    dadAddr = models.CharField(max_length=25,null=True,verbose_name="Father Address",help_text='Present address (if dead give last address)')
    dadPermAddr = models.CharField(max_length=25,null=True,verbose_name="Father Permanant Address",help_text='')
    momNam = models.CharField(max_length=20,null=True,verbose_name="Mother Name",help_text='')
    Momnat = models.CharField(max_length=10,null=True,verbose_name="Mother Nationality",help_text='')
    pbMom = models.CharField(max_length=10,null=True,verbose_name="Mother Place of Birth",help_text='')
    MomDesigAddr = models.CharField(max_length=25,null=True,verbose_name="Mother Occupation",help_text='Occupation(if employed give designation  &  official address)')
    MomAddr = models.CharField(max_length=25,null=True,verbose_name="Mother Address",help_text='Present address (if dead give last address)')
    MomPermAddr = models.CharField(max_length=25,null=True,verbose_name="Mother Permanant Address",help_text='')
    SpoNam = models.CharField(max_length=20,null=True,verbose_name="Spouse Name",help_text='')
    Sponat = models.CharField(max_length=10,null=True,verbose_name="Spouse Nationality",help_text='')
    pbSpof = models.CharField(max_length=10,null=True,verbose_name="Spouse Place of Birth",help_text='')
    SpoDesigAddr = models.CharField(max_length=25,null=True,verbose_name="Spouse Occupation",help_text='Occupation(if employed give designation  &  official address)')
    SpoAddr = models.CharField(max_length=25,null=True,verbose_name="Spouse Address",help_text='Present address (if dead give last address)')
    SpoPermAddr = models.CharField(max_length=25,null=True,verbose_name="Spouse Permanant Address",help_text='')
    Natlty = models.CharField(max_length=25,null=True,verbose_name="Your Nationality",help_text='')
    age = models.CharField(max_length=10,null=True,verbose_name="Age",help_text='')
    clsXage = models.CharField(max_length=10,null=True,verbose_name="Age at Matriculation (Standard X)",help_text='')
    birthPlace = models.CharField(max_length=10,null=True,verbose_name="BirthPlace",help_text='')
    birthdistrict = models.CharField(max_length=10,null=True,verbose_name="Birth District",help_text='')
    fatherDistrict = models.CharField(max_length=10,null=True,verbose_name="District of Father",help_text=' District and State to which your father      originally belongs')
    religion = models.CharField(max_length=15,null=True,verbose_name="Religion",help_text='')
    ScSt = models.CharField(max_length=4,null=True,verbose_name="Are you a member of a Scheduled Caste/ Scheduled Tribe ?",help_text='',choices=yesNo,default='No')
    scstName = models.CharField(max_length=25,null=True,verbose_name="if the answer is ‘Yes’, state the name threof.",help_text='')
    arrested = models.CharField(max_length=4,null=True,verbose_name="Have you ever been arrested ?",help_text='',choices=yesNo,default='No')
    prosecuted = models.CharField(max_length=4,null=True,verbose_name="Have you ever been prosecuted ?",help_text='',choices=yesNo,default='No')
    detention = models.CharField(max_length=4,null=True,verbose_name="Have you ever been kept under detention ?",help_text='',choices=yesNo,default='No')
    boundDown = models.CharField(max_length=4,null=True,verbose_name="Have you ever been bound down ?",help_text='',choices=yesNo,default='No')
    fined = models.CharField(max_length=4,null=True,verbose_name="Have you ever been fined by a court of law ?",help_text='',choices=yesNo,default='No')
    convicted = models.CharField(max_length=4,null=True,verbose_name="Have you ever been convicted by a court of law for any offence ?",help_text='',choices=yesNo,default='No')
    debarUniv = models.CharField(max_length=4,null=True,verbose_name="Have you ever been debarred From University ",help_text=' from any examination or rusticated by any University or any other educational authority / Institution ?',choices=yesNo,default='No')
    debatPubSer = models.CharField(max_length=4,null=True,verbose_name="Have you ever been debarred From Examinations ?",help_text='isqualified by any Public Service Commission from appearing at its examination / selection',choices=yesNo,default='No')
    pendCourt = models.CharField(max_length=4,null=True,verbose_name="Is any case pending against you in any court of law ?",help_text='or any other educational authority/ institution ',choices=yesNo,default='No')
    pendUniv = models.CharField(max_length=4,null=True,verbose_name="Is any case pending against you in any University ?",help_text='',choices=yesNo,default='No')
    crimeDesc = models.CharField(max_length=40,null=True,verbose_name="Description of Above",help_text='If the answer to any of above mentioned question is ‘Yes’, give full particulars of the case / arrest/ detention/ fine/ conviction/ sentence/ punishment etc. and / or the nature of the case pending in the Court/ University/ Education Authority etc., at time of filling up this form',default='No')
    localityRef1 = models.CharField(max_length=25,null=True,verbose_name="Reference 1",help_text='Name of two responsible persons of your locality or two references to whom you are known.')
    localityRef2= models.CharField(max_length=25,null=True,verbose_name="Reference 1",help_text='')
    place = models.CharField(max_length=25,null=True,verbose_name="Place ",help_text='')
    banKAcNo = models.CharField(max_length=25,null=True,verbose_name="Bank Account Number ",help_text='')

    Addr = models.CharField(max_length=100,null=True,verbose_name="Address",help_text='Present Address')
    contactNo = models.CharField(max_length=14,null=True,verbose_name="Contact Number",help_text='Mobile / Telephone Number')
    withEffectFrom = models.DateField(null=True, verbose_name="With Effect From", help_text='')

    IDAddChoice_options = (
        ('Permanent Address', 'Permanent Address'),
        ('Present Address', 'Present Address'),
        ('Both', 'Both')
    )

    IDAddChoice = models.CharField(max_length=25,
                                   null=True,
                                   verbose_name="Which Address to choose in id Card ",
                                   help_text='',
                                   choices=IDAddChoice_options,
                                   default='Both')
    IDName = models.CharField(max_length=40,
                              null=True,
                              verbose_name="Name to be displayed on ID Card",
                              help_text='')
    bloodgrp = models.CharField(max_length=20,
                                null=True,
                                verbose_name="Blood Group",
                                help_text='AB+/O-')
    EmercontactNo = models.CharField(max_length=14,
                                     null=True,
                                     verbose_name="Emergency Contact Number",
                                     help_text='Mobile / Telephone Number')

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = DumUser.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = DumUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.dumuser.save()
