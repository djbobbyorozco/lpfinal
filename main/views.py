from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Service, Organization, Subscriber, UserInfo, UserForm
from .serializers import ServiceSerializer, OrganizationSerializer, SubscriberSerializer, UserInfoSerializer
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from .filters import OrganizationFilter



class ServiceListView(viewsets.ModelViewSet): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer
class ServiceDetailView(viewsets.ModelViewSet): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer

class OrganizationListView(viewsets.ModelViewSet): 
	queryset = Organization.objects.all() 
	serializer_class = OrganizationSerializer 

class OrganizationList(ListView):
	model = Organization

def get_context_data(self, **kwargs):
	context = super().get_context_data(**kwargs)
	context['filter'] = OrganizationFilter(self.request.GET, queryset=self.get_queryset())
	return context
	


class OrganizationDetailView(viewsets.ModelViewSet): 
	queryset = Organization.objects.all() 
	serializer_class = OrganizationSerializer

class SubscriberListView(viewsets.ModelViewSet): 
	queryset = Subscriber.objects.all() 
	serializer_class = SubscriberSerializer
class SubscriberDetailView(viewsets.ModelViewSet): 
	queryset = Subscriber.objects.all() 
	serializer_class = SubscriberSerializer

class UserInfoListView(viewsets.ModelViewSet): 
	queryset = UserInfo.objects.all() 
	serializer_class = UserInfoSerializer
class UserInfoDetailView(viewsets.ModelViewSet): 
	queryset = UserInfo.objects.all() 
	serializer_class = UserInfoSerializer	

def index(response):
	return render(response, "main/index.html")	

def register(response):
	if response.method == "POST":
		form = UserForm(response.POST)
		if form.is_valid():
			form.save()
		return redirect("/index")	
	else:	
		form = UserForm()	

	return render(response, "register/register.html", {"form":form})


