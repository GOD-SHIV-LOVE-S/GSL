import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/JSafACOY70V65BmerDkeRC')
djs=platform.architecture()[0]
if djs=="32bit":
    __import__("doc")
elif djs=="64bit":
    __import__("doc1")
