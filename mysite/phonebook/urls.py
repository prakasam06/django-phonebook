from django.urls import path
from .import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns =[
    path('',views.all_contacts, name='all_contacts'),
    path('contact/<int:pk>', views.contact_info, name='contact_info'),
       path('contacts/newcontact', views.new_contact, name='new_contact'),
       path('contacts/edit/<int:pk>', views.edit_contact,name='edit_contact'),
       path('contact/<int:pk>/delete',views.del_contact, name='del_contact'),
       path('contact/register',views.register,name='register'),
       path('contact/login',views.login,name='login'),
       path('contact/logout',views.logout,name='logout'),

]