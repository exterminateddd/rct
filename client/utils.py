from json import load


def get_config():
    return load(open("config.json", "r+"))
