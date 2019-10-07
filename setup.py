import os
from setuptools import setup, find_packages

curdir = os.path.dirname(__file__)
with open(os.path.join(curdir, 'VERSION')) as vf:
    VERSION = vf.read().strip()

setup(
    name='hwinfrasdk',
    version=VERSION,
    author="Victor Ziv",
    author_email="vziv@infinidat.com",
    packages=find_packages(),
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    python_requires='>=3.6'
)
