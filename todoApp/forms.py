from django import forms
from .models import Task, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']

def widget_attrs(placeholder):
    return {"class": "u-full-width", "placeholder": placeholder}


def form_kwargs(widget, label="", max_length=64):
    return {"widget": widget, "label": label, "max_length": max_length}


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):

    username = forms.CharField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs("Username")))
    )
    password = forms.CharField(
        **form_kwargs(widget=forms.PasswordInput(attrs=widget_attrs("Password")))
    )

    def clean(self):
        # Don't check if we already have errors.
        if self.errors:
            return self.cleaned_data

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = User.objects.filter(username=username).first()

        # if not user or not user.check_password(password):
        #     raise forms.ValidationError("Incorrect username and/or password.")

        return self.cleaned_data