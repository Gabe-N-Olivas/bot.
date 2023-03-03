import os, inspect, discord
from lib import rsl

module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))

os.chdir(module_dir)

if not os.path.exists("logs"): rsl.initiate(module_dir)
print(os.path.realpath(os.path.dirname(module_path))) 

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("MTA4MDg5MzQ4NzgzNjMxOTgxNQ.G0kGhu.56Uj_9S0KrkWdqmOiqshppmBEqD2581G6Q4zkg")
