from django.forms import EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(required=True)  # django's form does not include email and we need it

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        # TODO: for some reason, password isn't getting stored. This is a fix for now, inspect later
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
