from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prénom'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

	def __init__(self,*args, **kwargs):
		super(SignUpForm,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].label = ""
		self.fields['username'].widget.attrs['placeholder'] = "Nom d'utilisateur"
		self.fields['username'].help_text = '<span class="form-text text-muted">Moins de 150 caractères. Lettres et nombres seulement.</span>'


		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].label = ""
		self.fields['password1'].widget.attrs['placeholder'] = "Mot de passe"
		self.fields['password1'].help_text = '<ul class="form-text text-muted"><li>Mot de passe différents des informations personnelles</li><li>Au moins 8 caractères</li><li>Pas de mots de passe communs</li><li>Ne pas utiliser que des chiffres</li></ul>'


		self.fields['password2'].widget.attrs['class'] = 'form-control'		
		self.fields['password2'].label = ""
		self.fields['password2'].widget.attrs['placeholder'] = "Confirmer le mot de passe"
		self.fields['password2'].help_text = '<span class="form-text text-muted">Retaper le mot de passe pour vérification.</span>'



class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')
	
	def __init__(self,*args, **kwargs):
		super(EditProfileForm,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].label = ""
		self.fields['username'].help_text = '<span class="form-text text-muted">Moins de 150 caractères. Lettres et nombres seulement.</span>'

		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].label = ""
		
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].label = ""

		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].label = ""