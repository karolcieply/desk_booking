from django import forms

from .models import Issue, Session


class IssuesForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. smitht24@gmail.com"})
    )

    class Meta:
        model = Issue
        fields = ["email", "issue", "user_agent"]


class SessionForm(forms.ModelForm):
    date = forms.DateField(disabled=False)
    # timeblock = forms.CharField(disabled=True)
    operator_licence = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter the number of your license (if applicable)"}), required=False
    )
    additional_info = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. I require assistance as I am unfamiliar with this workstation"}), required=False
    )

    class Meta:
        model = Session
        fields = ["date", "timeblock", "lab_workstation", "operator_licence", "additional_info"]
        # fields = ["date", "timeblock", "operator_licence", "additional_info"]        

    # REF: https://stackoverflow.com/questions/23690450/django-prevent-duplicates-for-users
    # def clean(self):
    #     # if Session.objects.filter(student=self.user, date=self.date).exists():
    #     #     raise forms.ValidationError(
    #     #         "Cannot schedule more than one session on a single day!"
    #     #     )
    #     if Session.objects.filter(date=self.date, timeblock=self.timeblock).exists():
    #         raise forms.ValidationError("That date & time is already booked!")
 