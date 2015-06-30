import yaml
from pkg_resources import resource_filename
from configurate import Configurate


config = Configurate()
config_file_name = resource_filename('fibonacci_service', 'config.yaml')

with open(config_file_name, 'r') as config_file:
    config.merge(yaml.load(config_file))
