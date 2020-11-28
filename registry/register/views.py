from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from lowuser.models import userdb,pancard,pincodedb,passport,votercard,marriagecert,license
from .forms import UserForm,LoginForm
from django.utils import timezone
from datetime import date
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from highuser.views import adminhome
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            aaid=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            dob=request.POST['dob']
            gender=request.POST['optradio']
            bloodg=request.POST['blood']
            address=request.POST['address']
            city=request.POST['city']
            state = request.POST['state']
            pincode=request.POST['pincode']
            mobileno=request.POST['mobileno']
            email=request.POST['email']
            user=authenticate(username=aaid,password=password)
            q = userdb(firstname=firstname, lastname=lastname, mobileno=mobileno, gender=gender, bloodgroup=bloodg,
                       birthdate=dob, address=address, city=city, state=state, pincode=pincode, email=email, aad=aaid,
                       app=0, user_id=user.id)
            q.save()
            subject = 'Thank You for Registration'
            message = 'Welcome CivilRegistry of AMRITA_UNIVERSITY\t\t' + 'Username:' + aaid + '\t\tPassword:' + password
            from_mail = 'CivilRegistry of AMRITA_UNIVERSITY'
            to_list = [email]
            send_mail(subject, message, from_mail, to_list, fail_silently=True)
            login(request, user)
            return redirect(home)
    else:
        form=UserForm()
    return render(request,'register.html',{'form':form})
def aadharregistration(request):
    if request.method=='POST':
        mobile=request.POST['mobileno']
        aadharno=request.POST['aadhar']
        password1=request.POST['password1']
        password2 = request.POST['password2']
        users=authenticate(username=aadharno,password=password1)

        n=userdb.objects.filter(mobileno=mobile).update(aad=aadharno)
        otp=6553
        '''subject = 'Thank You for Registration'
        message = 'Welcome CivilRegistry of AMRITA_UNIVERSITY\t\t' + 'Username:' + aadharno + OTP:+otp'\t\tPassword:' + password
        from_mail = 'civilregistry of AMRITA_UNIVERSITY'
        to_list =[ n.email]
        verify(otp,'otpverify')
        send_mail(subject, message, from_mail, to_list, fail_silently=True)'''
        return redirect(pancardregistration)
    else:
        return render(request,'login.html')

@login_required
def pancardregistration(request):
    if request.method=='POST':
        aadh= request.user.username
        n=userdb.objects.get(aad=aadh)
        panno1=request.POST['panno']
        major=request.POST['major']
        p=pancard(panno=panno1,majorstatus=major,pancardid=n)
        p.save()
        return redirect(home)
    else:
        aadh = request.user.username
        n = userdb.objects.get(aad=aadh)
        if pancard.objects.filter(pancardid_id=aadh).exists():
            q=pancard.objects.get(pancardid_id=aadh)
            return render(request,'panregister1.html',{'q' : q })
        else:
            return render(request,'panregister.html')

@login_required
def passportregistration(request):
    if request.method=='POST':
        aadh = request.user.username
        n = userdb.objects.get(aad=aadh)
        issuedate=request.POST['issdate']
        passportno=request.POST['passportno']
        nationality=request.POST['nationality']
        expiry=request.POST['expiry']
        residence=request.POST['residence']
        pincode=request.POST['pincode']
        u=pincodedb.objects.get(pin=pincode)
        city=u.city
        state=u.state
        passp=passport(passportid=n,dateissue=issuedate,passportno=passportno,nationality=nationality,dateexpiry=expiry,address=residence,pincode=pincode,city=city,state=state)
        passp.save()
        return redirect(home)
    else:
        aadh = request.user.username
        if passport.objects.filter(passportid_id=aadh).exists():
            w = passport.objects.get(passportid_id=aadh)
            return render(request,'passportregister1.html',{'w' : w })
        else:
            return render(request,'passportregister.html')


@login_required
def  votercardregistration(request):
    if request.method=='POST':
        aadh=request.user.username
        n=userdb.objects.get(aad=aadh)
        voterid=request.POST['voterid']
        vot=votercard(voter=n,voterid=voterid)
        vot.save()
        return redirect(home)

    else:
        aadh = request.user.username
        if votercard.objects.filter(voter_id=aadh).exists():
            q = votercard.objects.get(voter_id=aadh)
            return render(request, 'voteridregister1.html', {'q': q })
        else:
            return render(request, 'voteridregister.html')

@login_required
def  marriagecertregistration(request):
    if request.method=='POST':
        aadh=request.user.username
        n=userdb.objects.get(aad=aadh)
        certid=request.POST['certid']
        regoffno=request.POST['regno']
        mdate=request.POST['mdate']
        waadhar=request.POST['waadhar']
        saadhar=request.POST['saadhar']
        mc=marriagecert(marriageid=n,certno=certid,regoffid=regoffno,date=mdate,waadhar=waadhar,saadhar=saadhar)
        mc.save()
        return redirect(home)

    else:
        aadh = request.user.username
        if marriagecert.objects.filter(marriageid_id=aadh).exists():
            q = marriagecert.objects.get(marriageid_id=aadh)
            return render(request, 'marriageregister1.html', {'q': q})
        else:
            return render(request, 'marriageregister.html')

@login_required
def licenseregistration(request):
    if request.method=='POST':
        aadh= request.user.username
        n=userdb.objects.get(aad=aadh)
        licenseno=request.POST['licenseno']
        expirydate=request.POST['expirydate']
        type=request.POST['type']
        issuedate=request.POST['issuedate']
        p=license(licenseno=licenseno,expirydate=expirydate,type=type,issuedate=issuedate,licenseid=n)
        p.save()
        return redirect(home)
    else:
        aadh = request.user.username
        if license.objects.filter(licenseid_id=aadh).exists():
            q = license.objects.get(licenseid_id=aadh)
            return render(request, 'licenseregister1.html', {'q': q})
        else:
            return render(request, 'licenseregister.html')

@login_required
def viewall(request):
    aadh = request.user.username
    n=userdb.objects.get(aad=aadh)
    pan=pancard.objects.get(pancardid_id=aadh)
    pas=passport.objects.get(passportid_id=aadh)
    vote=votercard.objects.get(voter_id=aadh)
    marr=marriagecert.objects.get(marriageid_id=aadh)
    lic=license.objects.get(licenseid_id=aadh)
    return render(request,'viewusr.html',{'aadhar':n,'pan':pan,'pas':pas,'vote':vote,'marr':marr ,'lic' : lic})

@login_required
def editdetails(request):
    aadh = request.user.username
    n = userdb.objects.get(aad=aadh)
    pan = pancard.objects.get(pancardid_id=aadh)
    pas = passport.objects.get(passportid_id=aadh)
    vote = votercard.objects.get(voter_id=aadh)
    marr = marriagecert.objects.get(marriageid_id=aadh)
    lic = license.objects.get(licenseid_id=aadh)
    return render(request, 'useredit.html', {'aadhar': n, 'pan': pan, 'pas': pas, 'vote': vote, 'marr': marr,'lic' : lic},{})

@login_required
def t_edit(request):
    if request.method=="POST":
        aadh = request.user.username
        n = userdb.objects.get(aad=aadh)
        n.firstname=request.POST['firstname']
        n.lastname=request.POST['lastname']
        n.gender=request.POST['gender']
        n.address=request.POST['address']
        n.city=request.POST['city']
        n.state=request.POST['state']
        n.pincode=request.POST['pincode']
        n.mobileno=request.POST['mobile']
        n.save()
        return redirect(home)
    else:
        return HttpResponse('hi')


def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('adminview')
            else:
                login(request, user)
                return redirect('home')
        else:
            return redirect(login_view)
    else:
        return render(request,'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    aadh = request.user.username
    n = userdb.objects.get(aad=aadh)
    return render(request,'home.html',{'n':n })