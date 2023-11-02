from django import forms 
   

from .models import UserData,detail
   

class registerForm(forms.ModelForm): 
   
    class Meta: 
        model = UserData
        fields = "__all__" 

   

class authenticationForm(forms.Form): 
    email = forms.EmailField()
    password = forms.CharField(max_length=500)
      
class detailForm(forms.ModelForm):
     class Meta: 
        model = detail
        fields = "__all__" 
