from django.shortcuts import render
from form_exmple.forms import ContactForm


def contact(request):

    template_name = "form_exmple/contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            print("innser side of ContactForm")
            print(name, email, message)
            
            

    else:
        form = ContactForm()
    context = {"form": form}

    return render(request, template_name, context)
