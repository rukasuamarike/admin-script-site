from django import forms

from .models import Script
class ScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = {
            'code',
            'user',
        }



   # def clean_user(self,*args,**kwargs):
    #    user = self.cleaned_data.get("user")
    #    if "key" in user:
    #        return user
    #   if not "l" in user:
    #    raise forms.ValidationError("not valid user")
    #    else:
    #        raise forms.ValidationError("not valid user")
class RawScriptForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)
    user        = forms.CharField(widget=forms.HiddenInput)
