from django import forms

from .models import Employee, Project

class EmployeeForm(forms.ModelForm): #1
  class Meta: #2
    model = Employee #3
    fields = ["name", "date_joined", "date_of_birth", "phone_number", "position"] #4


class ProjectForm(forms.ModelForm): #5
  class Meta: #6
    model = Project #7
    fields = ["employee", "name", "start_date", "end_date", "amount"] #8
