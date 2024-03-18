from django import forms
from .models import customer,staff,products


class AddForm(forms.ModelForm):
    class Meta:
        model = customer

        fields = ('name','age','gender','email','phonenumber','username','password',)
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            
        } 


class AddForm(forms.ModelForm):
    class Meta:
        model = staff

        fields = ('name','age','gender','email','phonenumber','username','password','approval')
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            
        } 




class product_form(forms.ModelForm):
    class Meta:
        model = products

        fields = ('product_name','price','material','category','image')

        widgets = {
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'material':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

        