from django.forms import ModelForm
from .models import Blogpost

class BlogpostForm(ModelForm):
    class Meta:
        model = Blogpost
        fields = '__all__'