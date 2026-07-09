from django import forms


class AvailabilityForm(forms.Form):

    check_in = forms.DateField(
        required=True, input_formats=['%d-%m-%Y']
    )
    check_out = forms.DateField(
        required=True, input_formats=['%d-%m-%Y']
    )
