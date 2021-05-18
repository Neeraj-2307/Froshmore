from django.shortcuts import render,HttpResponse
from .models import user_query
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