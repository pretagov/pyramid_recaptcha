import colander
import requests
from colander import Invalid, null
from deform.widget import CheckedInputWidget


@colander.deferred
def deferred_recaptcha_widget(node, kw):
    request = kw['request']

    class RecaptchaWidget(CheckedInputWidget):
        template = 'recaptcha_widget'
        readonly_template = 'recaptcha_widget_readonly'
        requirements = ()
        url = "https://www.google.com/recaptcha/api/siteverify"
        headers = {'Content-type': 'text/plain'}

        def serialize(self, field, cstruct, readonly=False):
            if cstruct in (null, None):
                cstruct = ''
            # confirm = getattr(field, 'confirm', '')
            template = readonly and self.readonly_template or self.template
            settings = self.request.registry.settings
            public_key = settings['pyramid_recaptcha.public_key']
            return field.renderer(template,
                                  field=field,
                                  cstruct=cstruct,
                                  public_key=public_key)

        def deserialize(self, field, pstruct):
            if pstruct is null:
                return null
            response = pstruct.get('g-recaptcha-response') or ''
            if not response:
                raise Invalid(field.schema, 'No input')
            settings = self.request.registry.settings
            privatekey = settings['pyramid_recaptcha.private_key']
            remoteip = self.request.remote_addr
            request = requests.post(self.url, data={'secret': privatekey,
                                                    'response': response,
                                                    'remoteip': remoteip})
            if request.status_code != 200:
                raise Invalid(field.schema,
                              "There was an error talking to the recaptcha \
                              server ({0})".format(request.status_code))
            try:
                response = request.json()
            except ValueError as e:
                raise Invalid(field.schema,
                              "There was an error talking to the recaptcha \
                              server ({0})".format(e))
            valid = response['success']
            if valid is not True:
                # TODO: Should provide more meaningful error messages
                raise Invalid(field.schema, "Incorrect solution")
            return 'Verified'

    return RecaptchaWidget(request=request)
