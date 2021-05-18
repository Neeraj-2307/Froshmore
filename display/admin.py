from django.contrib import admin
from .models import hostel, user_query

# Register your models here.
admin.site.register(user_query)
admin.site.register(hostel)
