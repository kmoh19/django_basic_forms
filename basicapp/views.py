from django.shortcuts import render
from basicapp import forms

# Create your views here.

def index(request):
    return render(request,'basicapp/index.html',context='')


def form_name_view(request):
    form = forms.FormName()
    
    if request.method=='POST':
        form=forms.FormName(request.POST)
        
        if form.is_valid():
            
            #do dosomething!!
            
            print('validation success')
            print('NAME: ' + form.cleaned_data['name']) #cleaned data mapping object is only generated after is_valid() has been called on the form object
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: '+ form.cleaned_data['text'])
            
            
            
    return render(request,'basicapp/form_page.html',{'form':form})
