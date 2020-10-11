from django import forms
from .models import *

class EsepForm(forms.ModelForm):
    class Meta:
        model = Esep
        fields = ('whatsapp','email','telegram','description','file','deadline')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('email','question')