import configparser, os, inspect
from sys import platform

module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))

if platform == "win32" or  platform == "darwin":
    raise OSError("RSL was built with Linux in mind.")

config = configparser.ConfigParser()
config.read(f'{module_dir}/rsl.cfg')

def initiate(pwd):
    os.makedirs(f"{pwd}/logs")

def mklog():

    config["var"]["current-log-file"] = str(int(config["var"]["current-log-file"]) + 1)
    with open(f'{module_dir}/rsl.cfg') as conf:
        config.write(conf)
    print(config["var"]["current-log-file"])

mklog()

