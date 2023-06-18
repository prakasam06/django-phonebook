from django.shortcuts import render ,get_object_or_404
from django.shortcuts import redirect
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