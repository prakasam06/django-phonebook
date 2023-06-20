from django.shortcuts import render ,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from .models import contacts
from .forms import contact_form

# Create your views here.
def all_contacts(request):
    allcontacts = contacts.objects.all().order_by('name')
    return render(request, 'phonebook/all_contacts.html', {'allcontacts':allcontacts})

def contact_info(request, pk):
    contact = get_object_or_404(contacts, pk=pk)
    return render(request, 'phonebook/contact_info.html', {'contact': contact})

def new_contact(request):
    if request.method == "POST":
        form = contact_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('contact_info', pk=post.pk)
    else:
        form = contact_form()
    return render(request, 'phonebook/form.html', {'form': form})



def edit_contact(request, pk):
    contact = get_object_or_404(contacts, pk=pk)
    if request.method == "POST":
        form = contact_form(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact_info', pk=contact.pk)
    else:
        form = contact_form(instance=contact)
    return render(request, 'phonebook/form.html', {'form': form})

def del_contact(request,pk):
    contact = get_object_or_404(contacts, pk=pk)
    contact.delete()
    return redirect('all_contacts')

def register(request):
        
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
           
            if User.objects.filter(username=username).exists():
                        messages.info(request,'user already exixts')
                        return redirect('register')
            else: 
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname)
                    user.set_password(password)
                    user.save()
                    return redirect('login')
        else:
                    return render(request,"phonebook/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
          return redirect('all_contacts')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    else:
        return render(request,"phonebook/login.html")
  
    
def logout(request):
     auth.logout(request)
     return redirect('all_contacts')
