import os, inspect, discord
from lib import rsl

module_path = inspect.getfile(inspect.currentframe())
pwd = os.path.realpath(os.path.dirname(module_path))

os.chdir(pwd)

if not os.path.exists("logs"): rsl.initiate(pwd)
print(os.path.realpath(os.path.dirname(module_path))) 

with open('token.secret', 'r') as f:
    for i in f:  token = i 

bot.run(token)
