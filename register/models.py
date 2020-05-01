from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.

def register(response):
	if response.method == "POST":
		form = UserForm(response.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['userName']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			login(request, user)
		return redirect("/index")	
	else:	
		form = UserForm()	

	return render(response, "register/register.html", {"form":form})

# Create your models here.
# Create your models here.
