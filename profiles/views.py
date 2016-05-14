from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	context=locals()
	template='index.html'
	return render(request,template,context)

def courses(request):
	context=locals()
	template='courses.html'
	return render(request,template,context)

def atndnce(request):
	context=locals()
	template='atndnce.html'
	return render(request,template,context)

def pyth(request):
	context=locals()
	template='pyth.html'
	return render(request,template,context)
def cpp(request):
	context=locals()
	template='cpp.html'
	return render(request,template,context)
def java(request):
	context=locals()
	template='java.html'
	return render(request,template,context)

def about(request):
	context=locals()
	template='about.html'
	return render(request,template,context)

@login_required

def profile(request):
	user=request.user

	context={'user':user}
	template='profile.html'
	return render(request,template,context)