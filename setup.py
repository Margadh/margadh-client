import sys

from distutils.core import setup
from pip.req import parse_requirements

install_reqs = parse_requirements ('./requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]
setup (
    name = "Brainiac",
    version = "0.1",
    url = 'https://github.com/Margadh/margadh-client',
    author = 'Margadh',
    platforms = ('Any',),
    #FIXME: requires = reqs,
    packages = ['Brainiac'],
    scripts = ['brain.py'],
    package_dir = {'Brainiac': 'Brainiac'},
    package_data = {'Brainiac': ['templates/*',
                                 'static/css/*',
                                 'static/js/*']},
    data_files=[('/etc/brainiac/', ['etc/watchy/example.cfg'])],
)
