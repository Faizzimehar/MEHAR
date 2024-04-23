import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
Mehar=platform.architecture()[0]
if Mehar=="32bit":__import__("Mehar32")
elif Mehar=="64bit":__import__("Mehar64")
