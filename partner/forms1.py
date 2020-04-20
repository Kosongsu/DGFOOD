from django. forms import ModelForm
from .models import Store
from django import forms



# 배민 폼 강의
class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = (
            "name",
            "contact",
            "address",
            "description",
        )
        widgets = {
            "name": forms. TextInput(attrs={"class":"form-control"}),
            "contact": forms. TextInput(attrs={"class":"form-control"}),
            "address": forms. TextInput(attrs={"class":"form-control"}),
            "description": forms. Textarea(attrs={"class":"form-control"}),
        }
