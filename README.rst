=====
Nirvaris Pages
=====

A simple Django app to add a contact us form to your website.

It has a anti-spam engine.

Quick start
-----------

To install the contactform, use pip from git:

pip install git+https://github.com/nirvaris/nirvaris-contactform

1. Add "contactform" and the 'stylesnippet' to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
		'stylesnippet',
        'pages',
    )

2. You have to run makemigrations and migrate, as it uses the db to store the messages content. 

3. Copy the templates on the app's template folder to your application template folders
	These templates are used to render the pages. You should use them for your own style
	
4. You can access the page on your website by
	<your-url>/contact
	
	
5. you have to add the url to your urls file:  url(r'^contact/', include('contactform.urls')),