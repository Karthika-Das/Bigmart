from django.urls import path
from Webapp import views

urlpatterns=[
    path('',views.home_page,name="home"),
    path('about/',views.about_page,name="about"),
    path('contact/',views.contact_page,name="contact"),
    path('product/',views.our_product,name="product"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filter_page/<cat_name>/',views.filter_page,name="filter_page"),
    path('single_page/<int:proid>/',views.single_page,name="single_page"),
    path('register_page/',views.register_page,name="register_page"),
    path('register_save/',views.register_save,name="register_save"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delet_cart/<int:pid>',views.delet_cart,name="delet_cart"),
    path('user_page/',views.user_page,name="user_page"),
]