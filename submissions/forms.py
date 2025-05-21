from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('text_response', 'image_response')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_response'].required = False
        self.fields['image_response'].required = False
        
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text_response')
        image = cleaned_data.get('image_response')
        
        if not text and not image:
            raise forms.ValidationError("You must provide either text or an image response.")
        
        return cleaned_data
