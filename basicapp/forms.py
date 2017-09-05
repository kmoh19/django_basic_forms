from django import forms
from django.core import validators


# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError('NAME NEEDS TO START WITH Z')
  ##use check_for_z function to initialize field cla like this:  name=forms.CharField(validators[check_for_z])     

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='enter email again')
    text= forms.CharField(widget=forms.Textarea)# Whenever you specify a field on a form, Django will use a default widget that is appropriate to the type of data that is to be displayed. To find which widget is used on which field, see the documentation about Built-in Field classes
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
#     def clean_botcatcher(self): #clean_FIELD_NAME will automatically run to validate given FIELD...weird default method? triggered by POST?
#         botcatcher=self.cleaned_data['botcatcher']
#         if len(botcatcher)>0:
#             raise forms.ValidationError("GOTCHA BOT!")
#         return botcatcher

    def clean(self): #general clean
        all_clean_data=super().clean() # returns every clean data ..read up super...as in why not self.clean()---ah!!! because POST process may have overriden the clean function in the request object during inheritance
        email= all_clean_data['email']
        vmail= all_clean_data['verify_email']
        
        if email !=vmail:
            raise forms.ValidationError('Emails don\'t match!!')
        
        
        ####read up doc on validators
        
        
    
    