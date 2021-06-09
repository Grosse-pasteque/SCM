#ShortCut Manager {SCM} [0.3.0]

This program is use to add shortcuts that can launch apps or programs.
This program is dedicated to windows computers for the moment.

------


###Configuring ?

- add a config to the `config.json` file:
	```json
	{
		//any key combinaisons
		"key": ["ctrl+alt+n"],
		
		//run, write or press
		"mode": "run",
		
		//command to run , text to write , key(s) to press
		"command": "%windir%\\system32\\notepad.exe"
	}
	```
- for example the config used above will run notepad when `ctrl + alt + n` are pressed


###Windows Apps ?

- has you know some windows apps can't be executed from command prompt but with shell we can so in this file: [Here](./get_winapp_startcode.txt), I have put some informations of how to run windows app from this program
- for example this config run ZuneMusic:
	```json
	{
		"key": ["ctrl+alt+m"],
		"mode": "run",
		"command": "explorer.exe shell:AppsFolder\\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic"
	}
	```

###Running ?

- create a shortcut of the `main.pyw` file.
- put it in the `shell:startup` folder.

- set the run link to:
	```cmd
	"C:\Users\<user>\AppData\Local\Programs\Python\Python39\pythonw.exe" "C:\Users\<user>\<path>\main.pyw"
	```
- set the shortcut to admin mode (**key reading**).
- don't forget to replace:
	* `<user>` : computer username.
	* `<path>` : path to the `main.pyw` file.
- then when you will restart or click on this shortcut the program will run
