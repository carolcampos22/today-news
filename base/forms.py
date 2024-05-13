from django import forms
from base.models import Register

class RegisterNews(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['title', 'subtitle', 'description', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super(RegisterNews, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return None
        return image
    