from django import forms

class Userforms(forms.Form): #This class name will be used in views.py. The arguments are forms ( which is imported above) and Form ( which is class itself )
    num1=forms.CharField(label="Num1", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    num2=forms.CharField(label="Num2", required=False, widget=forms.TextInput)