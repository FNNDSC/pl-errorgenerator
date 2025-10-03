#!/usr/bin/env python
#                                                            _
# Simple App that crashes on purpose
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
import time
# import the Chris app superclass
from chrisapp.base import ChrisApp


Gstr_title = """
                                                         _             
                                                        | |            
  ___ _ __ _ __ ___  _ __ __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 / _ \ '__| '__/ _ \| '__/ _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/ |  | | | (_) | | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \___|_|  |_|  \___/|_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                          __/ |                                        
                         |___/                                         

"""

Gstr_synopsis = """

    NAME
    
        errorgenerator.py
        
    SYNOPSIS
    
        errorgenerator.py                                             \\
            [-v <level>] [--verbosity <level]                          \\
            [--version]                                                \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--errorType <typeError>]                                   \\ 
            [--customErrorMessage <message>]                             \\
            [--delayTime <secondsDelay>]                                 \\
            /tmp
            
            
    BRIEF EXAMPLE
    
        * To raise a ZeroDivisionError:
            python errorgenerator.py --errorType ZeroDivisionError /tmp
                                    
    DESCRIPTION
    
        `errorgenerator.py` basically crashes the program on purpose
        and throws a specific error
        
    ARGS
    
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number. 

        [--man]
        If specified, print (this) man page.
        
        [--meta]
        If specified, print plugin meta data.
        
        [--errorType <message>] 
        Type of error to raise.
        
        [--customErrorMessage <message>] 
        If specified, raise the error with the message.
        
        [--delayTime <secondsDelay>] 
        If specified, wait for specific seconds before raising the error.
        
"""


class ErrorGeneratorApp(ChrisApp):
    """
    Add prefix given by the --prefix option to the name of each input file.
    """
    PACKAGE = __package__
    TITLE = 'Error generator app'
    CATEGORY = 'utility'
    TYPE = 'ds'
    ICON = ''
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_CPU_LIMIT = 2000  # Override with millicore value as string, e.g. '2000m'
    MIN_MEMORY_LIMIT = 2000  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--errorType',
                          dest='errorType',
                          type=str,
                          optional=False,
                          help='raise this error',
                          default='')

        self.add_argument('--customErrorMessage',
                          dest='customErrorMessage',
                          type=str,
                          optional=True,
                          help='raise custom error message',
                          default='')

        self.add_argument('--delayTime',
                          dest='delayTime',
                          type=int,
                          optional=True,
                          help='wait before raising the error',
                          default=0)

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s\n' % self.get_version())

        parentClass = BaseException

        def iterateSubClasses(inpClass):
            for subClass in inpClass.__subclasses__():
                if subClass.__name__.lower() == options.errorType.lower():
                    time.sleep(options.delayTime)
                    raise subClass(options.customErrorMessage)
                iterateSubClasses(subClass)

        iterateSubClasses(parentClass)
        raise Exception('Invalid Error Type')

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)

