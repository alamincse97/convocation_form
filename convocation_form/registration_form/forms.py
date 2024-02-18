from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        }),
        max_length=30,
        required=True
    )
    father_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your father\'s name',
        }),
        max_length=30,
        required=True
    )
    mother_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your mother\'s name',
        }),
        max_length=30,
        required=True
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        choices=[('male', 'Male'), ('female', 'Female')],
        required=True
    )
    permanent_address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your permanent address',
            'rows':  2,
        }),
        required=True
    )
    present_address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your present address',
            'rows':  2,
        }),
        required=True
    )
    mobile_no = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your mobile number',
        }),
        max_length=12,
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address',
        }),
        required=True
    )
    id_no = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your ID number',
        }),
        max_length=10,
        required=True
    )
    degree_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your degree name',
        }),
        max_length=15,
        required=True
    )
    admission_session = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your admission session',
        }),
        max_length=15,
        required=True
    )
    passing_year = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        required=True
    )
    cgpa = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01',
        }),
        max_digits=5,
        decimal_places=2,
        required=True
    )

    class Meta:
        model = Applicant
        fields = [
            'name', 'father_name', 'mother_name', 'gender',
            'permanent_address', 'present_address', 'mobile_no', 'email',
            'id_no', 'degree_name', 'admission_session', 'passing_year', 'cgpa',
        ]