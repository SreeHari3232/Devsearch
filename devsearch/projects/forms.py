from django.db.models import fields
from django.db.models.base import Model
from django import forms
from django.forms import ModelForm, widgets
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image','description', 'demo_link', 'source_link' ,'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)
            
            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})