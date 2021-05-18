from django import http
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import user_query,hostel
# Create your views here.
def home_page(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            query = user_query(user_name = name,user_email = email,user_number = phone,user_querry = message)
            query.save()
            return render(request,"display/index.html")  
    return render(request,"display/index.html")

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already in use!')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Your email id already exists!')
                return redirect('/register/')
            else:        
                user = User.objects.create_user(first_name=name,username=username, email=email,password = pass1)
                user.save();
                return redirect('/login/')
                
        else:
            messages.info(request,"Password doesn't match") 
            return redirect('/register/')       
           

    else:
        return render(request,"display/register.html") 

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('/login/')    
    else:    
        return render(request,"display/login.html")    

def logout(request):
    auth.logout(request)
    return redirect('/')  

def about(request):
    return render(request,"display/aboutus.html")          


def rental(request):
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        ac = request.GET.get('ac',"off")
        visitor_entry = request.GET.get('visitor_entry',"off")
        water_cooler = request.GET.get('water_cooler',"off")
        room_cleaning = request.GET.get('room_cleaning',"off")
        if pincode:
            all_hostel_name = hostel.objects.filter(hostel_pincode = pincode)
            if all_hostel_name:
                demo = {
                    'hostel_list' : all_hostel_name,
                }
                return render(request,"display/rental.html",demo)
            return render(request,"display/pincode_not_found.html")
        if visitor_entry == "on":
            all_hostel_name = hostel.objects.filter(hostel_vistorentry=1)
        if ac == "on":
            all_hostel_name = hostel.objects.filter(hostel_ac=1)
        if water_cooler == "on":
            all_hostel_name = hostel.objects.filter(hostel_watercooler=1)
        if room_cleaning == "on":
            all_hostel_name = hostel.objects.filter(hostel_roomcleaning=1)
        if visitor_entry=="off" and ac=="off" and water_cooler=="off" and room_cleaning=="off" and pincode=="":
            all_hostel_name = hostel.objects.all()
        demo = {
                    'hostel_list' : all_hostel_name,
                }
        return render(request,"display/rental.html",demo)

    else:
        all_hostel_name = hostel.objects.all()
        demo2 = {
                'hostel_list' : all_hostel_name,
        }
    return render(request,"display/rental.html",demo2)


def tiffin(request):
    return render(request,"display/tiffin.html")
    

def misc(request):
    return render(request, "display/misc.html")