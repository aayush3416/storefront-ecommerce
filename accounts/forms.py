from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
    }))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     'placeholder': 'Email',
    #     'class': 'form-control'
    # }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'placeholder': 'First Name',
        #         'class': 'form-control'
        #     }),
        #     'last_name': forms.TextInput(attrs={
        #         'placeholder': 'Last Name',
        #         'class': 'form-control'
        #     }),
        #     'phone_number': forms.TextInput(attrs={
        #         'placeholder': 'Phone Number',
        #         'class': 'form-control'
        #     }),
        # }

    def __init__(self,*args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password do not match!"
            )