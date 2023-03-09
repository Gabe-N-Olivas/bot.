import configparser, os, inspect
from sys import platform
from datetime import datetime

# Get current date and time
now = datetime.now()

module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))
config = configparser.RawConfigParser()
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
    #if configparser.RawConfigParser("save", "use-timestamp"): time = now.strftime(configparser.RawConfigParser("save", "timestamp-strf"))
    #else: 
    time = None
    
    with open(f"{pwd}/logs/log.txt", mode='w', encoding='utf-8') as f:
        f.write(f"{time}, {input}")

print("RSL Loaded with no setup issues")