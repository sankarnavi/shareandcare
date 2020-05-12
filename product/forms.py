from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.db.models import options
from .models import Products
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "input100"}))
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=30, required=True)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('He is not there')
            if not user.check_password(password):
                raise forms.ValidationError('Password is wrong Bitch')
            if not user.is_active:
                raise forms.ValidationError('He is not Active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='email', required=True)
    confirmemail = forms.EmailField(label='Confirmemail', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=30, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'confirmemail',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        confirmemail = self.cleaned_data.get('confirmemail')
        if email != confirmemail:
            raise forms.ValidationError("emails should match")
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class ProductEntry(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'img', 'desc', 'expiry', 'category')
