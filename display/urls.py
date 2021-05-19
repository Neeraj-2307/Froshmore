from django.urls import path
from . import views

urlpatterns = [
	path("", views.home_page,name="home"),
	path("rental/",views.rental,name="rental"),
	path("tiffin/",views.tiffin,name="tiffin"),
	path("miscellaneous/",views.misc,name="misc"),
	path("laundry/",views.laundry,name="laundry"),
	path("library/",views.library,name="library"),
]