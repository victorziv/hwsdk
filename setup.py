import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))
# ===========================================


def read_version():
    with open(os.path.join(here, 'hwsdk', 'VERSION')) as vfr:
        version = vfr.read().strip()
    return version
# ___________________________________________


def write_version(version):
    with open(os.path.join(here, 'hwsdk', 'VERSION'), 'wb') as vfw:
        vfw.write(version)
# ===========================================


class TagsCommand(Command):
    user_options = []

    def initialize_options(self):
        """ Abstract method in parent class - must override"""
        pass
    # _______________________________________

    def finalize_options(self):
        """ Abstract method in parent class - must override"""
        pass
    # _______________________________________

    def run(self):
        version = read_version()
        os.system("git tag -a %s -m 'Version %s'" % (version, version))
        os.system("git push --tags")
        sys.exit()

# =============================================


class PyTest(TestCommand):
    # ____________________________

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True
    # ____________________________

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

# =============================================


class UploadCommand(Command):

    user_options = []
    # _______________________________________

    def initialize_options(self):
        """ Abstract method in parent class - must override"""
        pass
    # _______________________________________

    def finalize_options(self):
        """ Abstract method in parent class - must override"""
        pass
    # _______________________________________

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))
    # _______________________________________

    def remove_previous(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass
    # ________________________________________

    def build_pkg(self):
        self.status('Building source and wheel distribution...')
        os.system('{0} setup.py sdist bdist_wheel'.format(sys.executable))
    # ________________________________________

    def check_pkg(self):
        self.status('Checking built packages...')
        os.system('twine check dist/*')
    # ________________________________________

    def upload_pkg(self):
        self.status('Uploading the package to TestPyPi via Twine...')
        os.system('twine upload dist/*')
    # ________________________________________

    def bump_version_patch(self):
        self.status('Bumping version patch…')
        current_version = read_version()
        ver, patch = tuple([int(p.strip()) for p in current_version.split('.', 1)])
        new_patch = patch + 1
        new_version = '.'.join([str(p) for p in [ver, new_patch]])
        write_version(new_version.encode('utf-8'))
        os.system("git add hwsdk/VERSION && git commit -m 'Bump version to %s'" % new_version)
    # ________________________________________

    def run(self):
        try:
            self.remove_previous()
            self.bump_version_patch()
            self.build_pkg()
            self.check_pkg()
            self.upload_pkg()
        except OSError:
            pass

        sys.exit()
    # ________________________________________

# ===========================================


setup(
    name='hwsdk',
    version=read_version(),
    author="Victor Ziv",
    author_email="ziv.victor@gmail.com",
    url='https://github.com/victorziv/hwsdk',
    packages=find_packages(),
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    python_requires='>=3.6',

    # setup.py publish support
    cmdclass={
        'upload': UploadCommand,
        'publish': UploadCommand,
        'tags': TagsCommand,
        'test': PyTest,
    },

    extras_require={
        'testing': ['pytest'],
    }
)
