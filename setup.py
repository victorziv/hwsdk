import os
from setuptools import setup

here = os.path.dirname(__file__)

with open(os.path.join(here, 'VERSION')) as vf:
    VERSION = vf.read().strip()

setup(
    name='hwsdk',
    version=VERSION,
    author="Victor Ziv",
    author_email="ziv.victor@gmail.com",
    url='https://github.com/victorziv/hwsdk',
    packages=['hwsdk'],
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    python_requires='>=3.6'
)
