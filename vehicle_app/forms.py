from django import forms
from . models import Vehicle
from django.utils.translation import ugettext_lazy as _


class VehicleForm(forms.ModelForm):
    """ This is responsible for the creating a new or updating an existing Vehicle Instance in the database. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text

    class Meta:   
        model = Vehicle
        fields = "__all__"