from django import forms
from .models import Rating,Profile,Project
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_image = forms.ImageField(label = 'Image Field')


class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']

class RatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		
		exclude = ['user','image',]

class ImageForm(forms.ModelForm):
	class Meta:
		model = Project
		
		exclude = ['user']

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Project
		
		exclude = ['user']
