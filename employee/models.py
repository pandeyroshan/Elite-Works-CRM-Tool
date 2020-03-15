from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from projects.models import Projects
# Create your models here


class SuperVisors(models.Model):
    project = models.OneToOneField(Projects,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=50,blank=False)
    name = models.CharField('Name', max_length=250,blank=False)
    image = models.ImageField('Image',upload_to='Supervisor_Images',blank=True)
    mobile_number = models.CharField('Mobile Number',max_length=15)
    alter_number = models.CharField('Alternate Number',max_length=15)
    address = models.CharField('Address',max_length=400)
    resume = models.FileField(upload_to='Resume')
    aadhar_number = models.CharField('Aadhar Number',max_length=20)
    aadhar_photo = models.ImageField('Aadhar Card Photo',upload_to='Aadhar_photo',blank=True)
    pan_number = models.CharField('PAN Number', max_length=20)
    pan_photo = models.ImageField('PAN Card Photo',upload_to='PAN_Photo',blank=True)
    highest_qual = models.CharField('Highest Qualifications',max_length=200)
    highest_qual_photo = models.ImageField('Proof of Highest Qualification',upload_to='Highest_Qualification',blank=True)
    ten_certi = models.ImageField('10th Certificate',upload_to='ten_certi',blank=True)
    twelve_certi = models.ImageField('12th Certificate',upload_to='twelve_certi',blank=True)
    tech_certificate_name = models.CharField('Technical Certificate Name',max_length=300)
    tech_certi = models.ImageField('Technical Certificate',upload_to='tech_certi',blank=True)
    UAN_number = models.CharField('UAN Number',max_length=200)
    is_employee = models.BooleanField('Employee')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Supervisors List'
        verbose_name_plural = 'Supervisors List'
        unique_together = ('project', 'username',)

class labour(models.Model):
    project = models.ForeignKey(Projects,on_delete=models.CASCADE,null=True)
    name = models.CharField('Name', max_length=250,blank=False)
    image = models.ImageField('Image',upload_to='labour_Images',blank=True)
    mobile_number = models.CharField('Mobile Number',max_length=15)
    alter_number = models.CharField('Alternate Number',max_length=15)
    address = models.CharField('Address',max_length=400)
    resume = models.FileField(upload_to='Resume')
    aadhar_number = models.CharField('Aadhar Number',max_length=20)
    aadhar_photo = models.ImageField('Aadhar Card Photo',upload_to='Aadhar_photo',blank=True)
    pan_number = models.CharField('PAN Number', max_length=20)
    pan_photo = models.ImageField('PAN Card Photo',upload_to='PAN_Photo',blank=True)
    highest_qual = models.CharField('Highest Qualifications',max_length=200)
    highest_qual_photo = models.ImageField('Proof of Highest Qualification',upload_to='Highest_Qualification',blank=True)
    ten_certi = models.ImageField('10th Certificate',upload_to='ten_certi',blank=True)
    twelve_certi = models.ImageField('12th Certificate',upload_to='twelve_certi',blank=True)
    tech_certificate_name = models.CharField('Technical Certificate Name',max_length=300)
    tech_certi = models.ImageField('Technical Certificate',upload_to='tech_certi',blank=True)
    UAN_number = models.CharField('UAN Number',max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Labour List'
        verbose_name_plural = 'Labour List'

class Attendance(models.Model):
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    date = models.DateField('Start Date',default=timezone.now)
    labour = models.ForeignKey(labour,on_delete=models.CASCADE)
    A = 'A'
    B = 'B'
    C = 'C'
    status = [(A, 'A'),(B, 'B'),(C, 'C')]
    shift = models.CharField('Shift',max_length=10,choices=status,default=A)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.labour+self.is_present
    
    class Meta:
        verbose_name = 'Attandance'
        verbose_name_plural = 'Attandance'