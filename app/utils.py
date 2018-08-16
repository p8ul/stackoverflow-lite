from urllib.parse import urlparse


def db_config(config_file):
    """
    This function extracts postgres url
    and return database login information
    :param config_file: Configuration file
    :return: database login information
    """
    result = urlparse(config_file)
    config = {
        'database': result.path[1:],
        'user': result.username,
        'password': result.password,
        'host': result.hostname
    }
    return config


