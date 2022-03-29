from configuration import configuration

_framework = configuration.settings.get('Framework','active')
_filename = configuration.settings.get(_framework,'filename')

with open(_filename) as infile:
    exec(infile.read())