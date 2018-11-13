from django import forms

class StudyPlanForm(forms.Form):
    title = forms.CharField(help_text="Enter the title of the study plan.")
    
    # function to validate the data entered can be defined here ...
    def clean_title(self):
        data = self.cleaned_data['title']
    
    
    # remember to return something
    
        return data
