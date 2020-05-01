from django.db import models
from django.forms import ModelForm


# Create your models here.
class Organization(models.Model):
	orgCode = models.CharField(max_length=20)
	orgName = models.CharField(max_length=20)
	description = models.CharField(max_length=144)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	def __str__(self):
		return self.orgName
		

class Office(models.Model):
	officeName = models.CharField(max_length=20)
	officeCode = models.CharField(max_length=20)
	attribution = models.CharField(max_length=20)
	def __str__(self):
		return self.officeName

class Service(models.Model):
	serviceCode = models.CharField(max_length=20)
	serviceName = models.CharField(max_length=20)
	description = models.CharField(max_length=144)
	premium = models.CharField(max_length=20)
	allocation = models.CharField(max_length=20)
	def __str__(self):
		return self.serviceName

class Subscriber(models.Model):
	subID = models.CharField(max_length=20)
	subRequestDate = models.DateField()
	subStartDate = models.DateField()
	subEndDate = models.DateField()
	cancelationReason = models.CharField(max_length=50)
	subType = models.CharField(max_length=20)
	userName = models.CharField(max_length=20)
	beneficiaryID = models.CharField(max_length=20)
	def __str__(self):
		return self.subID

class Officer(models.Model):
	subID = models.CharField(max_length=20)
	officeCode = models.ForeignKey(Office, on_delete=models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()
	def __str__(self):
		return self.subID

class OrganizationMember(models.Model):
	orgCode = models.ForeignKey(Organization, on_delete=models.CASCADE)
	subID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	membershipStart = models.DateField()
	membershipEnd = models.DateField()
	nativeCountry = models.CharField(max_length=20)
	citizenship = models.CharField(max_length=20)
	y = 'yes'
	n = 'no'
	delegate = (
	(y, 'yes'),
	(n, 'no')
	)
	isdelegate = models.CharField(max_length=10, choices=delegate,)
	def __str__(self):
		return self.orgCode

class UserInfo(models.Model):
	userName = models.CharField(max_length=20, default='')
	fName = models.CharField(max_length=20)
	mName = models.CharField(max_length=20, null=True, blank=True)
	lName = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	address1 = models.CharField(max_length=20)
	address2 = models.CharField(max_length=20, null=True, blank=True)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=20)
	empName = models.CharField(max_length=20)
	homePhone = models.CharField(max_length=20, null=True, blank=True, default='')
	cellPhone = models.CharField(max_length=20, null=True, blank=True, default='')
	dob = models.DateField(null=True, blank=True )
	def _str_(self):
		return self.fName

class UserForm(ModelForm):
	class Meta:
		model = UserInfo
		fields = ["userName","fName", "mName", "lName", "address1", "address2", "city", "state", "zipcode", "homePhone", "cellPhone", "dob"]		
	

class SubscriptionType(models.Model):
	subName = models.ForeignKey(Subscriber, on_delete=models.CASCADE)


class TrasferredSubscription(models.Model):
	transferID = models.CharField(max_length=20)
	transferFrom = models.CharField(max_length=20)
	transferTo = models.CharField(max_length=20)
	requestDate = models.CharField(max_length=20)
