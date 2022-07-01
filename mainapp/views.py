from faulthandler import disable
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
from geopy.distance import geodesic
from numpy import take
from mainapp.models import infoofuser,equipment,equipment1,requests_apply
globalpost=''
def basepage(request):
    global globalpost
    print(globalpost)
    all_equ=equipment.objects.all()
    all_equipment_id=[i.equipment_id for i in all_equ]
    all_equ1=equipment1.objects.all()
    all_equipment_id1=[i.equipment_id for i in all_equ1]
    for i in all_equipment_id1:
        if i not in all_equipment_id:
            eq=equipment1.objects.filter(equipment_id=i)
            eq.delete()
    if request.user.is_authenticated and globalpost=='equipmentholder':
        return redirect('equipmentholderpage')
    elif request.user.is_authenticated and globalpost=='applicant':
        return redirect('applicantpage')
    return render(request,'basepage.html')
def loginpage(request):
    global globalpost
    if request.user.is_authenticated and globalpost=='equipmentholder':
        return redirect('equipmentholderpage')
    elif request.user.is_authenticated and globalpost=='applicant':
        return redirect('applicantpage')
    # return render(request,'loginpage.html')
    return render(request,'loginpage.html')
def registerpage(request):
    global globalpost
    if request.user.is_authenticated and globalpost=='equipmentholder':
        return redirect('equipmentholderpage')
    elif request.user.is_authenticated and globalpost=='applicant':
        return redirect('applicantpage')
    return render(request,'registerpage.html')
def handleregister(request):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if request.user.is_authenticated and globalpost=='equipmentholder':
        return redirect('equipmentholderpage')
    elif request.user.is_authenticated and globalpost=='applicant':
        return redirect('applicantpage')
    elif request.method == 'POST':
        # Get the post parameters
        alluser=infoofuser.objects.all()
        a=len(alluser)
        l=[int(i.user_id) for i  in alluser]
        while(a in l):
            a+=1
        Username = request.POST['username']
        Email = request.POST['email']
        Password=request.POST['password']
        Village= request.POST['village']
        Taluka= request.POST['taluka']
        District= request.POST['district']
        Latitude=request.POST['latitude']
        Longitude=request.POST['longitude']
        phoneno=request.POST['phoneno']
        #Check for errors
        if len(Username)<10:
            messages.error(request,'Error. Username Should be atleast 10 characters.')
            return redirect('registerpage')

        if not Username.isalnum():
            messages.error(request,'Error. Username Should only contain letters and numbers.')
            return redirect('registerpage')

        if(re.fullmatch(regex, Email)):
            pass
        else:
            messages.error(request,'Invalid Email')
        try:
            Latitude=float(Latitude)
            Longitude=float(Longitude)
        except ValueError:
            messages.error(request,'latitude and longitude value must be float')
            return redirect('registerpage')
        allusers=User.objects.all()
        for i in allusers:
            if(i.username==Username and i.password==Password):
                messages.error(request,"User already exists")
                return redirect('registerpage')
        myuser = User.objects.create_user(Username, Email, Password)
        myuser.save()
        newuser=infoofuser(username=Username, email=Email,password=Password,taluka=Taluka,district=District,village=Village,latitude=Latitude,longitude=Longitude,phone_no=phoneno,user_id=a)
        newuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('basepage')
    else:
        return HttpResponse('<h1>404-Error</h1>')
def handellogin(request):
    global globalpost
    if request.user.is_authenticated and globalpost=='equipmentholder':
        return redirect('equipmentholderpage')
    elif request.user.is_authenticated and globalpost=='applicant':
        return redirect('applicantpage')
    elif request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        Post=request.POST['post']
        globalpost=str(Post)
        print(globalpost)
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None and  Post=='equipmentholder':
            login(request, user)
            messages.success(request,"SuccessFully Logged In")
            return redirect('equipmentholderpage')
        elif(user is not None and Post=='applicant'):
            login(request, user)
            messages.success(request,"SuccessFully Logged In")
            return redirect('applicantpage')
    return HttpResponse("404- Not found")
def equipmentholderpage(request):
    global globalpost
    if request.user.is_authenticated and globalpost=='equipmentholder' :
        req=requests_apply.objects.filter(equipmentholder_name=request.user.username,request_status='Pending')
        his=requests_apply.objects.filter(equipmentholder_name=request.user.username,request_status='Accepted')
        params={}
        params['requests']=req
        params['history']=his
        return render(request,'equipmentholderpage.html',params)
    elif request.user.is_authenticated and globalpost=='applicant' :
        return redirect('applicantpage')
    else :
        return redirect('basepage')
def addequipment(request):
    global globalpost
    if request.user.is_authenticated and globalpost=='equipmentholder' :
        return render(request,'addequipment.html')
    elif request.user.is_authenticated and globalpost=='applicant' :
        return redirect('applicantpage')
    else :
        return redirect('basepage')
def add(request):
    if request.user.is_authenticated and globalpost=='equipmentholder' :
        if request.method == 'POST':
            Equipmentname=request.POST['equipmentname']
            Company=request.POST['company']
            Rent=request.POST['rent']
            Img1=request.FILES['img1']
            Img2=request.FILES['img2']
            Img3=request.FILES['img3']
            Img4=request.FILES['img4']
            Old=request.POST['old']
            allequipments=equipment.objects.all()
            l=[i.equipment_id for i in allequipments]
            print(l)
            a=len(allequipments)
            while(a in l):
                a+=1
            equipmentholder=infoofuser.objects.get(username=request.user.username)
            eq=equipment(username=request.user.username,password=request.user.password,latitude=equipmentholder.latitude,longitude=equipmentholder.longitude,village=equipmentholder.village,taluka=equipmentholder.taluka,district=equipmentholder.district,rent=Rent,image1=Img1,image2=Img2,image3=Img3,image4=Img4,equipmentname=Equipmentname,old=Old,company=Company,equipment_id=a,phone_no=equipmentholder.phone_no,equipmentholder_id=equipmentholder.user_id)
            eq.save()
            eq1=equipment1(username=request.user.username,password=request.user.password,latitude=equipmentholder.latitude,longitude=equipmentholder.longitude,village=equipmentholder.village,taluka=equipmentholder.taluka,district=equipmentholder.district,rent=Rent,image1=Img1,image2=Img2,image3=Img3,image4=Img4,equipmentname=Equipmentname,old=Old,company=Company,equipment_id=a,phone_no=equipmentholder.phone_no,equipmentholder_id=equipmentholder.user_id)
            eq1.save()
            messages.success(request,"Equipmet added successfully ")
            return redirect('addequipment')
    elif request.user.is_authenticated and globalpost=='applicant' :
        return redirect('applicantpage')
    else :
        return redirect('basepage')
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('basepage')
def deleteequipment(request):
    global globalpost
    if request.user.is_authenticated and globalpost=='equipmentholder' :
        allequipments=equipment.objects.filter(username=request.user.username)
        params={}
        params['allequipments']=allequipments
        return render(request,'deleteequipment.html',params)
    elif request.user.is_authenticated and globalpost=='applicant' :
        return redirect('applicantpage')
    else :
        return redirect('basepage')
def delete(request,slug):
    global globalpost
    if request.user.is_authenticated and globalpost=='equipmentholder':
        print(slug)
        eq=equipment.objects.filter(equipment_id=int(slug))
        eq.delete()
        return redirect('deleteequipment')
    return redirect('basepage')
def applicantpage(request):
    global globalpost
    if request.user.is_authenticated and globalpost=='applicant':
        eq=equipment1.objects.all()
        applicant=infoofuser.objects.get(username=request.user.username)
        lat_long=(applicant.latitude,applicant.longitude)
        eq=list(sorted(eq, key = lambda x:geodesic(lat_long,(x.latitude,x.longitude)).km))
        params={}
        params['allequipments']=eq
        return render(request,'applicantpage.html',params)
    return redirect('loginpage')
def requests(request):
    if request.user.is_authenticated and globalpost=='applicant' :
        req=requests_apply.objects.filter(applicant_name=request.user.username)
        params={}
        params['requests']=req
        return render(request,'requests.html',params) 
    elif request.user.is_authenticated and globalpost=='equipmentholder':
        return redirect('equipmentholderpage')
    else :
        return redirect('basepage')
def apply(request,slug):
    if request.user.is_authenticated and globalpost=='applicant' :
        print(slug)
        takedate=request.POST['take']
        givedate=request.POST['give']
        takedate=takedate.split('-')
        givedate=givedate.split('-')
        takedate='/'.join(takedate)
        givedate='/'.join(givedate)
        print(takedate)
        print(givedate)
        d1 = datetime.strptime(takedate, "%Y/%m/%d")
        d2 = datetime.strptime(givedate, "%Y/%m/%d")

        # difference between dates in timedelta
        delta = d2 - d1
        totaldays=int(delta.days)
        already=requests_apply.objects.filter(applicant_name=request.user.username,equipment_id=int(slug))
        print(len(already))
        if len(already)==0 :
            equ=equipment1.objects.get(equipment_id=int(slug))
            totalrent=equ.rent*totaldays
            applicant=infoofuser.objects.get(username=request.user.username)
            req=requests_apply(applicant_name=request.user,applicant_village=applicant.village,applicant_taluka=applicant.taluka,applicant_district=applicant.district,applicant_phone=applicant.phone_no,equipment_name=equ.equipmentname,equipment_id=int(slug),equipmentholder_phone_no=equ.phone_no,equipmentholder_name=equ.username,equipmentholder_village=equ.village,equipmentholder_taluka=equ.taluka,equipmentholder_district=equ.district,rent=equ.rent,take_date=takedate,give_date=givedate,total_rent=totalrent,applicant_id=applicant.user_id,equipmentholder_id=equ.equipmentholder_id)
            req.save()
            return redirect('applicantpage')
    elif request.user.is_authenticated and globalpost=='equipmentholder':
        return redirect('equipmentholderpage')
    else :
        return redirect('basepage')
def denied_request(request,slug):
    if request.user.is_authenticated and globalpost=='applicant' :
        return redirect('applicantpage')
    elif request.user.is_authenticated and globalpost=='equipmentholder':
        slug=slug.split(',')
        slug=[int(i) for i in slug]
        print(slug)
        req=requests_apply.objects.filter(equipment_id=slug[0],applicant_id=slug[1])
        print(req)
        req.delete()
        return redirect('equipmentholderpage')
    else :
        return redirect('basepage')
def accept_request(request,slug):
    if request.user.is_authenticated and globalpost=='equipmentholder':
        slug=slug.split(',')
        slug=[int(i) for i in slug]
        equ1=equipment1.objects.filter(equipment_id=slug[0])
        req=requests_apply.objects.get(equipment_id=slug[0],applicant_id=slug[1],request_status='Pending')
        all_req=requests_apply.objects.filter(equipment_id=slug[0])
        for i in all_req:
            if(i!=req):
                i.delete()
        req.request_status='Accepted'
        equ1.delete()
        req.save()
        return redirect('equipmentholderpage')
    elif request.user.is_authenticated and globalpost=='applicant':
        return redirect('applicantpage')
    else :
        return redirect('basepage')
    # req=requests_apply.objects.filter(equipment_id=int(slug))
