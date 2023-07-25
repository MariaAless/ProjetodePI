from django.forms import ModelForm
from django import forms
from .models import Task



class TaskForm(forms.ModelForm):


    class Meta:
        model = Task
        fields=['title','description', "imagem"]
        

        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control' }),
                    'description': forms.Textarea(attrs={'class': 'form-control' }),
                    'imagem': forms.FileInput(attrs={'class': 'form-control' }),
                    
                

                }
