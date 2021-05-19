from django import http
from django.shortcuts import render,HttpResponse
from .models import user_query,hostel,tiffinservice
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
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        if pincode:
            all_tiffin_name = tiffinservice.objects.filter(tiffinservice_pincode = pincode)
            if all_tiffin_name:
                demo = {
                    'tiffin_list' : all_tiffin_name,
                }
                return render(request,"display/tiffin.html",demo)
            return render(request,"display/pincode_not_found.html")
        all_tiffin_name = tiffinservice.objects.all()
        demo = {
                    'tiffin_list' : all_tiffin_name,
                }
        return render(request,"display/tiffin.html",demo)

    else:
        all_tiffin_name = tiffinservice.objects.all()
        demo2 = {
                'tiffin_list' : all_tiffin_name,
        }
    return render(request,"display/tiffin.html",demo2)
    

def misc(request):
    return render(request, "display/misc.html")

def laundry(request):
    return HttpResponse("laundary details here")

def library(request):
    return HttpResponse("library details here")
