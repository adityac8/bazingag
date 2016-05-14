from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from .forms import contactForm
# Create your views here.

def contact(request):
	form=contactForm(request.POST or None)
	if form.is_valid():
		comment=form.cleaned_data['comment']
		name=form.cleaned_data['name']
		subject='Message form MYSITE.com'
		message='%s %s' %(comment , name)
		emailFrom=form.cleaned_data['email']
		emailTo=[settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
	context=locals()
	template='contact.html'
	return render(request,template,context)
