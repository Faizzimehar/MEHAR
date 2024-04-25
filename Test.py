import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
Test=platform.architecture()[0]
if Test=="32bit":__import__("Test32")
elif Test=="64bit":__import__("Test64")
