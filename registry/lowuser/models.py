from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userdb(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE);
    firstname=models.CharField(max_length=30);
    lastname=models.CharField(max_length=30);
    mobileno=models.IntegerField();
    gender=models.IntegerField();
    bloodgroup=models.CharField(max_length=5);
    birthdate=models.DateField();
    address=models.CharField(max_length=2000);
    city=models.CharField(max_length=30);
    state=models.CharField(max_length=30);
    pincode=models.IntegerField();
    email=models.EmailField();
    aad=models.CharField(max_length=13,primary_key=True);
    app=models.IntegerField();

    def __str__(self):
        return self.aad
class votercard(models.Model):
    voter=models.OneToOneField(userdb,on_delete=models.CASCADE)
    voterid=models.CharField(max_length=13,primary_key=True);
    def __str__(self):
        return self.voterid
class passport(models.Model):
    passportid= models.OneToOneField(userdb,on_delete=models.CASCADE);
    dateissue=models.DateField();
    passportno=models.CharField(max_length=20,primary_key=True);
    nationality=models.CharField(max_length=30);
    dateexpiry=models.DateField();
    address=models.CharField(max_length=300);
    city=models.CharField(max_length=30);
    state=models.CharField(max_length=20);
    pincode=models.IntegerField();
    def __str__(self):
        return self.passportno
class marriagecert(models.Model):
    marriageid=models.OneToOneField(userdb,on_delete=models.CASCADE);
    certno=models.CharField(max_length=20,primary_key=True);
    regoffid=models.CharField(max_length=20);
    date=models.DateField();
    waadhar=models.CharField(max_length=13);
    saadhar=models.CharField(max_length=13);
    def __str__(self):
        return self.certno
class pancard(models.Model):
    pancardid=models.OneToOneField(userdb,on_delete=models.CASCADE);
    panno=models.CharField(max_length=20,primary_key=True);
    majorstatus=models.IntegerField();
    def __str__(self):
        return self.panno
class license(models.Model):
    licenseid=models.OneToOneField(userdb,on_delete=True);
    licenseno=models.CharField(max_length=20);
    expirydate=models.DateField();
    type=models.IntegerField();
    issuedate=models.DateField();
    def __str__(self):
        return self.licenseno

class pincodedb(models.Model):
    pin=models.CharField(max_length=7,primary_key=True);
    city=models.CharField(max_length=40);
    state=models.CharField(max_length=30);
    def __str__(self):
        return self.pin

