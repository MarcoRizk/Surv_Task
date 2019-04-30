from django.forms import ModelForm
from .models import LinkedinQuery


class LinkedinQueryForm(ModelForm):
    """"
    The form for the LinkedinQuery model
    """
    class Meta:
        model = LinkedinQuery
        fields = ["country", "company", "department"]
