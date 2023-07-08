from django import forms
from .models import Dulcinea

class DulcineaForm(forms.ModelForm):
      class Meta:
            model = Dulcinea
            
            fields = ('date_1', 'user', 'desc', 'RS_rate', 'GM_rate', 'event_image')

            widgets = {
                  'date_1': forms.SelectDateWidget(attrs= {'class':'form-control'}),
                  'user': forms.Select(attrs= {'class':'form-control'}),
                  'desc': forms.Textarea(attrs= {'class':'form-control', 'placeholder':"Description"}),
                  'RS_rate': forms.TextInput(attrs= {'class':'form-control'}),
                  'GM_rate': forms.TextInput(attrs= {'class':'form-control'}),
            }
       