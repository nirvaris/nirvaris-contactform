import pdb
import uuid

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import ContactMessage



class ContactForm(forms.ModelForm):
    
    send_to_me = forms.BooleanField(required=False, label=_('Send a copy to me'))

    anti_spam_token = forms.CharField(widget=forms.HiddenInput())
    anti_spam_hidden = forms.CharField(widget=forms.HiddenInput())
    anti_spam_no_hidden = forms.CharField(required=False,label='')

    class Meta:
        model = ContactMessage
        fields = [
            'name','email','message','send_to_me'
        ]
        labels = {
            'name':_('Your Name'),
            'email':_('Your E-mail'),
            'message':_('Message'),
            'send_to_me':_('Send a copy to me')
        }

    def anti_spam(self):
        
        spam_token = uuid.uuid4()
        
        self.initial['anti_spam_token'] = str(spam_token)
        self.initial['anti_spam_no_hidden'] = str(spam_token) 
        self.initial['anti_spam_hidden'] = ''  