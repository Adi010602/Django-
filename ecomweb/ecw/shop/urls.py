from . import views
from django.urls import path


urlpatterns = [
   path("",views.index, name="ShopHome"),
   path("about/",views.about, name="aboutUs"),
   path("contact/",views.contact, name="contact"),
   path("tracker/",views.tracker, name="tracker"),
   path("search/",views.search, name="search"),
   path("products/<int:myid>", views.productView, name="ProductView"),
   path("Checkout/",views.checkout, name="checkout"),

]
