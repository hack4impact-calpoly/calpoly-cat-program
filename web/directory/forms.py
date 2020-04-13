from django import forms

class ClientForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    birthday = forms.DateField(label='DOB')
    location = forms.CharField(label='Location', max_length=50)
    
