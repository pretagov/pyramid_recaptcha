import os

from setuptools import find_packages
from setuptools import setup

project = 'pyramid_recaptcha'
version = '1.0.1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'deform',
    'colander',
    'requests',
    'pyramid']

desc = 'A pyramid/deform widget implementing googles recaptcha widget.'

setup(
    name=project,
    version=version,
    description=desc,
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Pylons',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: User Interfaces'],
    keywords='pyramid deform recaptcha captcha',
    author='Jon Pentland, PretaGov Ltd',
    author_email='jon.pentland@pretagov.co.uk',
    url='https://github.com/pretagov/pyramid_recaptcha.git',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={})
