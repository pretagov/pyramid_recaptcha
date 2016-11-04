from pkg_resources import resource_filename
from deform import Form
from recaptcha import deferred_recaptcha_widget
import logging; logger = logging.getLogger('recaptcha')


def includeme(config):
    logger.info('Loading recaptcha search path')
    loader = Form.default_renderer.loader
    loader.search_path = (resource_filename('pyramid_recaptcha', 'templates')) + loader.search_path
