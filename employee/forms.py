from django import forms
from .models import Employee

class AddEmployee(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['id','first_name','last_name','dept','salary','bonus','role','phone','hire_date']
    
        widgets={
            'hire_date':forms.DateInput(attrs={'id':'datepicker'}),
        }