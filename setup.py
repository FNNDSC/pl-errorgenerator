from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()


setup(
      name             =   'errorgenerator',
      # for best practices make this version the same as the VERSION class variable
      # defined in your main plugin app class
      version          =   '1.0.2',
      description      =   'A ChRIS app that crashes on purpose',
      long_description =   readme,
      author           =   'Arnav Nidumolu',
      author_email     =   'arnav.nidumolu@gmail.com',
      url              =   'https://github.com/FNNDSC/pl-errorgenerator',
      packages         =   ['errorgenerator'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      license          =   'MIT',
      zip_safe         =   False,
      python_requires  = '>=3.6',
      entry_points     = {
        'console_scripts': [
            'errorgenerator = errorgenerator.__main__:main'
            ]
        }
     )
