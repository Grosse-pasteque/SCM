import subprocess
class MessageBox:
	def __init__(self, msg='', button=4, style=64, title=''):
		with open('mbf.vbs', 'w') as f:
			f.write(f'Dim WShell\nSet WShell = WScript.CreateObject("WScript.Shell")\nWShell=MsgBox("{msg}",{button}+{style},"{title}")')
			f.close()
		subprocess.Popen('mbf.vbs', shell=True)