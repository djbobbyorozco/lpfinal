from django.urls import path, include
from . import views
from .views import OrganizationList
from rest_framework import routers
from django.contrib.auth.views import LoginView




router = routers.DefaultRouter()
router.register('Organizations', views.OrganizationListView)
router.register('Services', views.ServiceListView)
router.register('Subscribers', views.SubscriberListView)
router.register('UserInfo', views.UserInfoListView)

urlpatterns = [
	path('', include(router.urls)),       
	path("index/", views.index, name="index"),
	path('accounts/', include('django.contrib.auth.urls')),
	path('register/', views.register, name="register"),
	path('login/', LoginView.as_view(), name='login'),
	path('members/', OrganizationList.as_view()),
]

