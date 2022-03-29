import os
import configparser

class configuration:

    file = 'settings.ini'

    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read(os.path.join(os.getcwd(),file),encoding='utf-8')
    settings.sections()