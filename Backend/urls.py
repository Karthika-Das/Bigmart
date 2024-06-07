from django.urls import path
from Backend import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('category_page/', views.category_page, name="category_page"),
    path('save_page/', views.save_page, name="save_page"),
    path('display_page/', views.display_page, name="display_page"),
    path('edit_page/<int:bigid>/', views.edit_page, name="edit_page"),
    path('update_page/<int:bigid>/', views.update_page, name="update_page"),
    path('delete_page/<int:bigid>/', views.delete_page, name="delete_page"),
    path('login_page/', views.login_page, name="login_page"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('product_page/', views.product_page, name="product_page"),
    path('save_product/', views.save_product, name="save_product"),
    path('product_display/', views.product_display, name="product_display"),
    path('product_edit/<int:proid>/', views.product_edit, name="product_edit"),
    path('update_product/<int:proid>/', views.update_product, name="update_product"),
    path('delete_product/<int:proid>/', views.delete_product, name="delete_product"),
    path('data_details/', views.data_details, name="data_details"),
    path('delete_contact/<int:delid>', views.delete_contact, name="delete_contact"),

]