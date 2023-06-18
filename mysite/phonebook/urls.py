from django.urls import path
from .import views

urlpatterns =[
    path('',views.all_contacts, name='all_contacts'),
    path('contact/<int:pk>', views.contact_info, name='contact_info'),
       path('contacts/newcontact', views.new_contact, name='new_contact'),
       path('contacts/edit/<int:pk>', views.edit_contact,name='edit_contact'),
       path('contact/<int:pk>/delete',views.del_contact, name='del_contact'),
]