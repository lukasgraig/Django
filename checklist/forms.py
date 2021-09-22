from django import forms
from .models import CheckList


class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = "__all__"