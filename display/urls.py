from django import urls
from django.conf.urls import url
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
	path("laundry/",views.laundary,name="laundry"),
	path("library/",views.lib,name="library"),
	path("aboutus/",views.about,name="aboutus"),
	path("message/",views.message,name="message"),
	path("description_page",views.description_page,name="description_page"),
    #path("description_page/<int:myid>",views.description_page,name="description_page"),
]
