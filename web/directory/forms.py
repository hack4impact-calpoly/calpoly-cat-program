from django import forms
from directory.models import Cat

class ClientForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    birthday = forms.DateField(label='DOB')
    location = forms.CharField(label='Location', max_length=50)
    
class IntakeForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = [
            'name', 'gender', 'age', 'description', 'breed', 'itype', 'status',
            'arrival_date', 'arrival_details', 'medical_history', 'vaccinations',
            'is_microchipped', 'flea_control_date', 'deworming_date', 'fiv_felv_date', 
            'special_needs', 'personality', 'more_personality', 'comments', 
            'personal_exp'
        ]
