from django.core import mail
from django.test import TestCase


from ..email import send_contact_message
from ..models import ContactMessage

class ContactMessageTestCase(TestCase):

    def setUp(self):
        ...
        
    def tearDown(self):
        ...                  

    def test_send_contact_message(self):
        
        
        mail.outbox = []
        
        contact_message = ContactMessage(name='JB', email='juliano.binder@gmail.com', message='This is a test')

        send_contact_message(contact_message)
        
        self.assertEqual(len(mail.outbox), 1,'No email sent')
        
        #response = c.post(reverse('contact'),{
        #    'name':'JB',
        #    'email':'juliano.binder@gmail.com',
        #    'message':'This is a Test',
        #})
        