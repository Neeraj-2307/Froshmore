from django.contrib import admin
from .models import hostel, laundry, library, tiffin_service, user_querry

# Register your models here.
admin.site.register(user_querry)
admin.site.register(hostel)
admin.site.register(tiffin_service)
admin.site.register(laundry)
admin.site.register(library)