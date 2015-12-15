import pdb

from django.core import mail
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait




class SeleniumTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(SeleniumTestCase, cls).setUpClass()
        cls.browser = webdriver.Firefox()
        cls.site_url = cls.live_server_url
        
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(SeleniumTestCase, cls).tearDownClass()     

    def test_send_contact_message(self):
        
        mail.outbox = []
        
        browser = self.browser
        
        browser.get(self.site_url + reverse('contact'))
        
        input_name = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//input[@id='id_name']"))

        input_email = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//input[@id='id_email']"))
        
        input_message = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//textarea[@id='id_message']"))        

        input_name.send_keys('Jack')
        input_email.send_keys('jack@daniels.com')
        input_message.send_keys('Jack killer propper rock and roller drink')            
        
        submit_button = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//button[@id='id_button_submit_contact_form']"))
        #pdb.set_trace()
        submit_button.click()
        

        self.assertEqual(len(mail.outbox), 1,'No email sent')

    def test_send_contact_message_ajax(self):
        
        mail.outbox = []
        
        browser = self.browser
        
        browser.get(self.site_url + reverse('form-tag'))
        
        input_name = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//input[@id='id_name']"))

        input_email = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//input[@id='id_email']"))
        
        input_message = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//textarea[@id='id_message']"))        

        input_name.send_keys('Jack')
        input_email.send_keys('jack@daniels.com')
        input_message.send_keys('Jack killer propper rock and roller drink')            
        
        submit_button = WebDriverWait(browser, 10).until( lambda browser: browser.find_element_by_xpath("//button[@id='id_button_submit_contact_form']"))
        #pdb.set_trace()
        submit_button.click()
        
        self.assertEqual(len(mail.outbox), 1,'No email sent')

        