import keyboard
import subprocess
import json
from time import sleep
from messagebox import MessageBox

configs = json.loads(open('config.json').read())

def call(command):
	p = subprocess.Popen(command, shell=True)
	sleep(0.1)
	p.terminate()

file = '\\'.join(__file__.split('\\')[:-1])+'\\config.json'
MessageBox(f"ShortCut Manager correclty enable with config '{file}'.", 4, 64, 'ShortCut Manager')

for config in configs:
	if config['mode'] == 'run':
		for key in config['key']:
			keyboard.add_hotkey(
				key,
				call,
				(config['command'],)
			)

	elif config['mode'] == 'text':
		for key in config['key']:
			keyboard.add_hotkey(
				key,
				keyboard.write,
				(config['command'],)
			)

	elif config['mode'] == 'press':
		for key in config['key']:
			keyboard.add_hotkey(
				key,
				keyboard.press,
				(config['command'],)
			)

keyboard.wait()