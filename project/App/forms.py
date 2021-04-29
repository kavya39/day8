from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from App.models import HandiCrafts,User,Worker,Category

class RegForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"
		}))
	class Meta:
		model=User
		fields=['username']
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter username",
			}),
		}
class CraftsForm(forms.ModelForm):
	class Meta:
		model=HandiCrafts
		fields=["category_type","quantity","price","im"]
		widgets = {
		"category_type":forms.Select(attrs= {
			"class":"form-control",
			"placeholder":"select category",
			}),
		"quantity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Quantity",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Price",
			}),
		}



class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']

class WorkerForm(forms.ModelForm):
	class Meta:
		model=Worker
		fields=["profession","name" ,"phno","gender","Email"]
		widgets={
		"profession":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"select category "}),
		"name":forms.TextInput(attrs=
			{
			"class":"form-control",
			"placeholder":"Enter your name"
			}),
		"gender":forms.Select(attrs={"class":"form-control"}),
		"Phone no":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter your phone number"}),
		"Email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}),
		}
