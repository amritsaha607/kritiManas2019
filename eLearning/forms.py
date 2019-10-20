from django import forms
from .models import *

passwordWidget = {'password': forms.PasswordInput()}

class RegisterFormStudent(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		widgets = passwordWidget

class RegisterFormClub(forms.ModelForm):
	class Meta:
		model = Club
		fields = '__all__'
		widgets = passwordWidget

class LoginFormStudent(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['username', 'password']
		widgets = passwordWidget

class LoginFormClub(forms.ModelForm):
	class Meta:
		model = Club
		fields = ['username', 'password']
		widgets = passwordWidget

class LoginFormDepartment(forms.ModelForm):
	class Meta:
		model = Department
		fields = ['username', 'password']
		widgets = passwordWidget

class CreateTut(forms.ModelForm):
	class Meta:
		model = CourseTutorial
		fields = ['series_title', 'course']


class NewDocLibraryForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ['file', 'filename', 'doc_type', 'sem', 'course', 'dept']