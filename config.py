import json

with open('config.json', 'r') as f:
   config = json.load(f)
 
username = config['username']
password = config['password']
