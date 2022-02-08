import subprocess


notepad = subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
notepad.wait()
print(notepad.poll())
