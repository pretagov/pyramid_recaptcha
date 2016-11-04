from pkg_resources import resource_filename
from deform import Form
from recaptcha import deferred_recaptcha_widget  # noqa


def add_search_path():
    loader = Form.default_renderer.loader
    loader.search_path = (resource_filename('pyramid_recaptcha', 'templates'),)\
        + loader.search_path


def includeme(config):
    add_search_path()
