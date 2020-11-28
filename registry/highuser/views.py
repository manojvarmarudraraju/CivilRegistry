from django.shortcuts import render
from lowuser.models import *
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import verify

# Create your views here.
@login_required
def approveUser(request):
    q=userdb.objects.filter(app__in=[0])
    w=userdb.objects.filter(app__in=[1])
    return render(request,'adminview.html',{'user1':q,'user2':w })
@login_required
def viewuser(request,userdb_aad):
    if request.method=='POST':
        app=request.POST['app']
        e=userdb.objects.get(aad=userdb_aad)
        e.app=app
        e.save()
        aadh = request.user.username
        date=timezone.now()
        a=verify(adminid=aadh,userid=userdb_aad,veridate=date)
        a.save()
        return  redirect(approveUser)
    else:
        e=get_object_or_404(userdb, pk = userdb_aad)
        if e.app==0:
            return render(request,'appuser.html',{'app':e })
        else:
            return render(request, 'appuser1.html', {'app': e})

@login_required
def deleteuser(request,userdb_aad):
    e=userdb.objects.get(aad=userdb_aad)
    if votercard.objects.filter(voter_id=userdb_aad).exists():
        q=votercard.objects.get(voter_id=userdb_aad)
        q.delete()
    if passport.objects.filter(passportid_id=userdb_aad).exists():
        w=passport.objects.get(passportid_id=userdb_aad)
        w.delete()
    if marriagecert.objects.filter(marriageid_id=userdb_aad).exists():
        q=marriagecert.objects.get(marriageid_id=userdb_aad)
        q.delete()
    if pancard.objects.filter(pancardid_id=userdb_aad).exists():
        q=pancard.objects.get(pancardid_id=userdb_aad)
        q.delete()
    if license.objects.filter(licenseid_id=userdb_aad).exists():
        q=license.objects.get(licenseid_id=userdb_aad)
        q.delete()
    e.delete()
    return redirect(approveUser)

@login_required
def adminhome(request):
    aadh = request.user.username
    n = userdb.objects.get(aad=aadh)
    return render(request,'adminhome.html',{'aad':n })

@login_required
def reportuser(request):
    if request.method=='POST':
        ad=request.POST['aad']
        if userdb.objects.filter(aad=ad).exists():
            n = userdb.objects.get(aad=ad)
            pan = pancard.objects.get(pancardid_id=ad)
            pas = passport.objects.get(passportid_id=ad)
            vote = votercard.objects.get(voter_id=ad)
            marr = marriagecert.objects.get(marriageid_id=ad)
            lic = license.objects.get(licenseid_id=ad)
            return render(request, 'showuser.html',{'aadhar': n, 'pan': pan, 'pas': pas, 'vote': vote, 'marr': marr, 'lic': lic})
        else:
            return redirect(reportuser)
    else:
        return render(request,'adminsearch.html');