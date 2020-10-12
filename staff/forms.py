from .models import Staff
from django import forms


class StaffCreate(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['is_approved_by_register']
