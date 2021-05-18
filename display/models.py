from django.db import models

# Create your models here.

class user_query(models.Model):
    user_name=models.CharField(max_length=50, default="name")
    user_email=models.EmailField(max_length=50,default="email")
    user_number=models.CharField(max_length=20,default="0")
    user_querry=models.CharField(max_length=1000,default="querry")

    def __str__(self):
        return self.user_name + " " + self.user_email

class  hostel(models.Model):
    hostel_name=models.CharField(max_length=80, default="name")
    hostel_address=models.CharField(max_length=120, default="address")
    hostel_state=models.CharField(max_length=30, default="state")
    hostel_city=models.CharField(max_length=30, default="city")
    hostel_rent=models.IntegerField(default="rent")
    hostel_deposit=models.IntegerField(default="deposit")
    hostel_contactnumber=models.IntegerField(default="contact number")
    hostel_pincode=models.IntegerField(default="pincode")
    hostel_area=models.CharField(max_length=120, default="area")
    hostel_mess=models.IntegerField(default="0/1")
    hostel_mealtype=models.CharField(max_length=120, default="mealtype")
    hostel_ac=models.IntegerField(default="0/1")
    hostel_vistorentry=models.IntegerField(default="0/1")
    hostel_watercooler=models.IntegerField(default="0/1")
    hostel_roomcleaning=models.IntegerField(default="0/1")