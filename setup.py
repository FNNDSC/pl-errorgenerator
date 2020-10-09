
import sys
import os

# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")

from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()


setup(
      name             =   'errorgenerator',
      # for best practices make this version the same as the VERSION class variable
      # defined in your main plugin app class
      version          =   '1.0.0',
      description      =   'A ChRIS app that crashes on purpose',
      long_description =   readme(),
      author           =   '',
      author_email     =   '@gmail.com',
      url              =   'https://github.com/FNNDSC/pl-errorgenerator',
      packages         =   ['errorgenerator'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['errorgenerator/errorgenerator.py'],
      license          =   'MIT',
      zip_safe         =   False
     )