from django.urls import path
from . import views

urlpatterns = [
	path("", views.home_page,name="home"),
	path("rental/",views.rental,name="rental"),
	path("tiffin/",views.tiffin,name="tiffin"),
	path("miscellaneous",views.misc,name="misc"),
	path("register/",views.register,name="register"),
	path("login/",views.login,name="login"),
	path("logout/",views.logout,name="logout"),
]