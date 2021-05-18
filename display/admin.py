from django.contrib import admin
from .models import hostel, laundry, library, tiffin_service, user_query

# Register your models here.
admin.site.register(user_query)
admin.site.register(hostel)
admin.site.register(tiffin_service)
admin.site.register(laundry)
admin.site.register(library)