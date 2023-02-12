import os, inspect
from lib import rsl
module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))

os.chdir(module_dir)

if not os.path.exists("logs"): rsl.initiate(module_dir)