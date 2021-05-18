from django.db import models

# Create your models here.

class user_query(models.Model):
    user_name=models.CharField(max_length=50, default="name")
    user_email=models.EmailField(max_length=50,default="email")
    user_number=models.CharField(max_length=20,default="0")
    user_querry=models.CharField(max_length=1000,default="querry")

    def _str_(self):
        return self.user_name + " " + self.user_email
class hostel(models.Model):
    hostel_name=models.CharField(max_length=120, default="name")
    hostel_state=models.CharField(max_length=30, default="state")
    hostel_city=models.CharField(max_length=30, default="city")
    hostel_area=models.CharField(max_length=120, default="area")
    hostel_pincode=models.IntegerField(default="pincode")
    hostel_address=models.CharField(max_length=120, default="address")
    hostel_rent=models.IntegerField(default="rent")
    hostel_deposit=models.IntegerField(default="deposit")
    hostel_contactnumber=models.IntegerField(default="contact number")
    hostel_mess=models.IntegerField(default="0/1")
    hostel_mealtype=models.CharField(max_length=120, default="mealtype")
    hostel_ac=models.IntegerField(default="0/1")
    hostel_vistorentry=models.IntegerField(default="0/1")
    hostel_watercooler=models.IntegerField(default="0/1")
    hostel_roomcleaning=models.IntegerField(default="0/1")  
    hostel_description=models.TextField(max_length=500, default="")
    hostel_images1=models.ImageField(upload_to='display/img/hostel_images',default="" )
    hostel_image2=models.ImageField(upload_to='display/img/hostel_images', default="" )
    def _str_(self):
        return self.hostel_name 

class  tiffin_service(models.Model):
    tiffin_service_name=models.CharField(max_length=80, default="name")
    tiffin_service_state=models.CharField(max_length=30, default="state")
    tiffin_service_city=models.CharField(max_length=30, default="city")
    tiffin_service_area=models.CharField(max_length=120, default="")
    tiffin_service_address=models.CharField(max_length=200, default="address")
    tiffin_service_pincode=models.IntegerField(default="00")
    tiffin_service_price=models.IntegerField(default="0")
    tiffin_service_contactnumber=models.IntegerField(default="+91")
    tiffin_service_mealtype=models.CharField(max_length=120, default="veg")
    tiffin_service_mealsperday=models.IntegerField(default=3)
    tiffin_service_description=models.TextField(max_length=600, default="")
    tiffin_service_images1=models.ImageField(upload_to='display/img/tiffin_service_images' ,default="")
    tiffin_service_image2=models.ImageField(upload_to='display/img/tiffin_service_images' ,default="")
    def _str_(self):
        return self.tiffin_service_name 

class  laundry(models.Model):
    laundry_name=models.CharField(max_length=80, default="name")
    laundry_state=models.CharField(max_length=30, default="state")
    laundry_city=models.CharField(max_length=30, default="city")
    laundry_area=models.CharField(max_length=120, default="")
    laundry_address=models.CharField(max_length=120, default="address")
    laundry_pincode=models.IntegerField(default="00")
    laundry_price=models.IntegerField(default="0")
    laundry_contactnumber=models.IntegerField(default="+91")
    laundry_description=models.TextField(max_length=200, default="")
    laundry_images1=models.ImageField(upload_to='display/img/laundry_images', default="" )
    def _str_(self):
        return self.laundry_name 

class  library(models.Model):
    library_name=models.CharField(max_length=80, default="name")
    library_address=models.CharField(max_length=120, default="address")
    library_state=models.CharField(max_length=30, default="state")
    library_city=models.CharField(max_length=30, default="city")
    library_pincode=models.IntegerField(default="00")
    library_area=models.CharField(max_length=120, default="")
    library_deposit=models.IntegerField(default="0")
    library_contactnumber=models.IntegerField(default="+91")
    library_pincode=models.IntegerField(default="00")
    library_area=models.CharField(max_length=120, default="")
    library_description=models.TextField(max_length=200, default="")
    library_images1=models.ImageField(upload_to='display/img/library_images', default="" )
    def _str_(self):
        return self.library_name