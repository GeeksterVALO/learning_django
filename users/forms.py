from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['nickname', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Nickname')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = User.objects.filter(email=username).first() or User.objects.filter(nickname=username).first()
            if user is None:
                raise forms.ValidationError('Invalid login credentials')
            self.cleaned_data['username'] = user.nickname

        return super().clean()

class UserEditForm(forms.ModelForm):
    full_name = forms.CharField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['nickname', 'email', 'full_name', 'bio']

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if User.objects.filter(nickname=nickname).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("This nickname is already taken.")
        return nickname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("This email is already taken.")
        return email

class FavoriteGameForm(forms.Form):
    game_id = forms.IntegerField(widget=forms.HiddenInput())