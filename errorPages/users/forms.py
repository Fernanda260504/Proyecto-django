import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'required': True,
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required': True,
                    'maxlength': '100',  
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellidos',
                    'required': True,
                    'maxlength': '100',  
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de control',
                    'required': True,
                    'maxlength': '10',  
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                    'min': '18',  
                    'max': '100',  
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono',
                    'required': True,
                    'maxlength': '10',  
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                    'minlength': '8', 
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirmar contraseña',
                    'required': True,
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@utez.edu.mx'):
            raise forms.ValidationError("El correo electrónico debe ser de la UTEZ.")
        return email

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if not re.match(r'^\d{5}[a-zA-Z]{2}\d{3}$', control_number):
            raise forms.ValidationError("La matrícula debe seguir el formato: 5 dígitos, 2 letras, 3 dígitos.")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if len(tel) != 10 or not tel.isdigit():
            raise forms.ValidationError("El teléfono debe contener exactamente 10 dígitos.")
        return tel

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"\d", password) or not re.search(r"[@$!%?&]", password):
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres, 1 mayúscula, 1 número y 1 carácter especial.")
        return password

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if len(surname) < 3:
            raise forms.ValidationError("El apellido debe tener al menos 3 caracteres.")
        return surname

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 100:
            raise forms.ValidationError("La edad debe estar entre 18 y 100 años.")
        return age

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class CustomUserLoginForm(AuthenticationForm):
    pass
