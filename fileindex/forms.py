from django import forms
class StudyPlanForm(forms.Form):
    title = forms.TextField(help_text="Enter the title of the study plan.")
    
    # function to validate the data entered can be defined here ...