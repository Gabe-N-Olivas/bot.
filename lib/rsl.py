import configparser, os, inspect
from sys import platform

module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))
config = configparser.ConfigParser()
config.read(f'{module_dir}/rsl.cfg')

if platform == "win32" and config.get("debug","FORCE_WIN_LOAD") == False:
    raise OSError("RSL was built with POSIX in mind. You can attempt to run this by setting FORCE_LOAD_WIN to True")

if __name__ == "__main__" and config.get("debug","FORCE_RUN_MAIN") == False: raise Exception("RSL is module.")

def initiate(pwd):
    try: os.makedirs(f"{pwd}/logs")
    except FileNotFoundError: 
        print("RSL could not find your save directory. Defaulting to global save on /var/rsl/logs/log.txt")
        pwd = config.get("save","global-save")
    with open(f"{pwd}/logs/log.txt", 'a'):
        os.utime(f"{pwd}/logs", None)

def mklog(pwd, input):
    with open(f"{pwd}/logs/log.txt", mode='w', encoding='utf-8') as f:
        f.write(input)

print("RSL Loaded with no setup issues")