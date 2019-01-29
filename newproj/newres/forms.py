from django import forms
from newres.models import Logindata,Question,Userdata

class Userform(forms.ModelForm):
    class Meta:
        model=Userdata
        exclude=["group"]
        labels = {
            'contactno': _('Contact Number'),
            'year_of_study': _('Year of study'),
        }
