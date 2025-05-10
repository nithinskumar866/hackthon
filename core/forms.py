from django import forms
from .models import Donation
from .models import NGO


from .models import NGO

class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = '__all__'
        widgets = {
            'mission': forms.Textarea(attrs={'rows': 3}),
            'street_address': forms.Textarea(attrs={'rows': 3}),
            'agreed_to_terms': forms.CheckboxInput(),
        }
        labels = {
            'has_transportation': 'Does your organization have pickup capability?'
        }
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
        widgets = {
            'pickup_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'expiry_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'description': forms.Textarea(attrs={'rows': 3}),
            'pickup_address': forms.Textarea(attrs={'rows': 3}),
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pickup_time'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['expiry_time'].input_formats = ['%Y-%m-%dT%H:%M']