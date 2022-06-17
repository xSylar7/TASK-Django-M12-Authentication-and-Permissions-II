from django import forms
from django.contrib.auth import get_user_model

from movies import models

User = get_user_model()


class MovieForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(
        User.objects.all(),
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = models.Movie
        fields = ["name", "plot", "created_by"]
