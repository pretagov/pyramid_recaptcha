pyramid_recaptcha
=================

pyramid_recaptcha is a deform widget for Pyramid, implementing the google recaptcha service. See (https://developers.google.com/recaptcha/)

Installation
------------
Get a public and private API key from google. https://developers.google.com/recaptcha/

Add `pyramid_recaptcha` in `install_requires` in your `setup.py`.
and edit `production.ini` in your Pyramid application to add::

    pyramid.includes =
        ...
        pyramid_recaptcha

    pyramid_recaptcha.public_key = your_public_key
    pyramid_recaptcha.private_key = your_private_key


Add the widget to a form::

    import colander
    from pyramid_recaptcha import deferred_recaptcha_widget

    class MyForm(colander.MappingSchema):

        captcha = colander.SchemaNode(colander.String(),
                                      title='Verify you are human',
                                      widget=deferred_recaptcha_widget)


Bind the `request` variable when rendering the form::

    MyForm().bind(request=self.request)
