from django import forms
from .models import UserDetails

class MyDataForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user', 'phoneNum', 'userPlan']

