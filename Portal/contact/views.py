from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm

def contacts(request):
    tittle = 'contact'
    confirm_message = None
    form = contactForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        tittle = "Thanks!"
        confirm_message = "Thanks for the message. we will get right back to you."
        form = None
    context = {'tittle': tittle, 'form':form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request, template, context)