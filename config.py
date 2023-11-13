import os
from configparser import ConfigParser


cur_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(cur_dir, "config.ini")
config = ConfigParser()
config.read(config_path)


def get_db_path():
    return config['database']['path']
