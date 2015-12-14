#Nirvaris Contact Form


Here is our Django app to add a "contact us" form to your website.

It has a built in anti-spam engine. 

It uses the follow dependecies from Nirvaris:

- [Nirvaris Default Theme](https://github.com/nirvaris/nirvaris-theme-default)

#Quick start


To install the contactform, use pip from git:

```
pip install git+https://github.com/nirvaris/nirvaris-contactform
```

- Add _contactform_ and the _themedefault_ to your INSTALLED_APPS setting like this::

```
    INSTALLED_APPS = (
        ...
        'themedefault',
        'contactform',
    )
```

- The app has a model to store the messages sent, so you have to run migrate. 

- You have to add the url to your urls file:

```
url(r'^contact/', include('contactform.urls')),
```

- As it sends emails for account activation and forgot password, you have to setup your SMTP details in your settings. [Django docs for sending emails](https://docs.djangoproject.com/en/1.9/topics/email/)

```
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
```
- You have to add your email asddress to your settings

```
NV_SEND_TO = '' # optional: the subject of the email
NV_EMAIL_FROM = '' # The address which the email will be sent from
NV_CONTACTFORM_SUBJECT = '' # The subject for the email to be sent

```

- There are two ways to use it. You can access the page on your website by the url. It will use the look and feel of the theme

```	
<your-url>/contact
```
- Or you can use a template tag, so the form will use ajax requests to send the message.

```
{% load form_tag %}
{% form_tag %}
```
