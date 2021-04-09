from django import forms

# creating a form
class InputForm(forms.Form):

    cht_msg = forms.CharField(max_length = 300, help_text="Input your description here..")
