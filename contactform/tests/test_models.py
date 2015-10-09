from django.test import TestCase


from ..models import ContactMessage

class ContactMessageTestCase(TestCase):

    def setUp(self):
        ...
    def tearDown(self):
        ...                  

    def test_contact_message(self):
        contact_message = ContactMessage(name='Johnny Walker',email='johnny@walker.com',message='10 years old')
        