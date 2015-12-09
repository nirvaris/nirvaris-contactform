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

- There are two ways to use it. You can access the page on your website by the url. It will use the look and feel of the theme

```	
<your-url>/contact
```
- Or you can use a template tag, so the form will use ajax requests to send the message.

```
{% load form_tag %}
{% form_tag %}
```
