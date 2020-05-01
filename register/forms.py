from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from main.models import UserInfo, UserForm


class UserForm(UserForm):
	dob = forms.DateField(help_text="Required. Format: YYYY-MM-DD")
	email = forms.EmailField(help_text="Required valid email format E.g. johndoe@email.com")
	class Meta:
		model = UserInfo
		fields =["userName","fName", "mName", "lName", "email", "address1", "address2", "city", "state", "zipcode", "homePhone", "cellPhone", "dob"]
		labels ={"userName" : "User Name", "fName" : "First Name", "mName":"Middle Name", "lName" : "Last Name", "email" : "Email", "address1": "Address1", "address2":"Address2", "city":"City", "state": "State", "zipcode":"Zipcode/Postal Code", "homePhone": "Home Phone", "cellPhone": "Cell Phone", "dob":"Date Of Birth"

		}
# Create your models here.