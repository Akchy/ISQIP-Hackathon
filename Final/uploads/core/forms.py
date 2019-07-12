from django import forms

from uploads.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name','email','phrase','categories', 'phone','address', 'description', 'document', )
