from django import forms


class CreateLaptopForm(forms.Form):
    image = forms.FileField(required=False)
    model = forms.CharField(max_length=64)
    cost = forms.IntegerField(min_value=0)
    description = forms.CharField(widget=forms.Textarea())
    condition = forms.CharField(max_length=50)
    laptop_types = forms.CharField(max_length=100)
    release_year = forms.IntegerField()




