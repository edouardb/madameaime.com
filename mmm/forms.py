from django import forms

import models


class RegistrationForm(forms.ModelForm):
    password_repeat = forms.CharField(widget = forms.PasswordInput)

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password and password_repeat and password != password_repeat:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data

    def save(self):
        return models.User.objects.create_user(
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )

    class Meta:
        model = models.User
        fields = ('email', 'password')

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = models.Newsletter
        exclude = ('date', 'active')
