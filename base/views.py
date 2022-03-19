from django.shortcuts import render,redirect
from django.views import View
from .models import Contact
# Create your views here.


class ContactsList(View):
    template_name = "base/index.html"

    def get(self,request):
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        contacts = Contact.objects.filter(full_name__icontains =q)
        context = {"contacts":contacts,}
        return render(request,self.template_name,context)

class NewContact(View):
    template_name = "base/add.html"
    def post(self,request):
        form = request.POST.get
        new_contact = Contact.objects.create(
            full_name = form('fullname'),
            email = form("email"),
            address = form("address"),
            phone_number = form('phone_number'),
            relation = form("relation"),
        )
        new_contact.save()
        return redirect("home")

    def get(self,request):
        return render(request,self.template_name,{})

def updateContact(request,pk):
    template_name = "base/update.html"
    instance = Contact.objects.get(id=pk)
    if request.method == "GET":
        return render(request,template_name,{"instance":instance,})

    if request.method == "POST":
        form = request.POST.get
        instance = Contact.objects.get(id=pk)
        instance.full_name = form('fullname')
        instance.email = form("email")
        instance.address = form("address")
        instance.phone_number = form('phone_number')
        instance.relation = form("relation")

        instance.save()
        return redirect("home")


def deleteContact(request,pk):
    template_name = "base/delete.html"
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("home")
    return render(request,template_name,{'contact':contact,})



def contactDetail(request,pk):
    contact = Contact.objects.get(id=pk)
    template_name = "base/contact-profile.html"
    context = {"contact":contact,}
    
    return render(request,template_name,context)

