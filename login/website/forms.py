from django import forms
from .models import task, message


class userloginform(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()



class addprojectform(forms.Form):
    Pname = forms.CharField(max_length=400)
    Pdescription = forms.CharField(max_length=3000)
    Cname = forms.CharField(max_length=300)
    Cdetails = forms.CharField(max_length=4000)
    Pdeadline = forms.CharField(max_length=100)
    Pstartdate = forms.CharField(max_length=100)
    Pmanagedby = forms.CharField(max_length=400)
    Pcontract = forms.CharField(max_length=2000)
    Ptextresource = forms.CharField(max_length=6000)


Technology_CHOICES = (
    ('JAVA', 'JAVA'),
    ('PYTHON', 'PYTHON'),
    ('MATLAB', 'MATLAB'),
    ('JULIA', 'JULIA'),
    ('R', 'R')
)


class addtaskform(forms.ModelForm):
    Ttechnology = forms.ChoiceField(choices=Technology_CHOICES)

    class Meta():
        model = task
        fields = ("__all__")


class messageform(forms.ModelForm):
    class Meta():
        model = message
        fields = "__all__"

