import pdb


from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.edit import FormView
# Create your views here.

from .forms import ContactForm
from .models import ContactMessage


class ContactView(FormView):
    template_name = 'contact-form.html'
    form_class = ChangeUserDetailsForm
    success_url = 'contact'
    
    def form_valid(self, form):

        form.save()
        messages.success(self.request,_('New details where saved'))

        return super(ChangeUserDetailsView, self).form_valid(form)    