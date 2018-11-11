"""
#####################################
 PPP   Y   Y    OO     SSSS
 P  P   Y Y    O  O    S
 PPP     Y     O  O    SSSS
 P       Y     O  O       S
 P       Y      OO     SSSS     v3.6
#####################################
"""
import time
import TerminalGui as gui
import os

gui.clear()
gui.tprint(gui.formatCodes.FAIL, __doc__.strip())
time.sleep(3)

os.system("dialog --backtitle \"Installing PyOS\"        --title \"PyOS Will Now Install On System\"        --yesno \"\n\nData Will Not be Erased.\nInstall?\" 10 30")
gui.drawDialog("---------------LOG IN----------------", "UserName [  ROOT _ ]\nLogin", Width=50)
if input("Key:") != "hellopyos":
    print("Wrong Key! Try Again...")
    if input("Key:") != "hellopyos":
        print("Wrong Key! Locking...")
        while True:
            time.sleep(1)
import AppManager
from PreferenceManager import PreferenceManager

print("Starting Home App...")
time.sleep(3)

while True:
    AppPref = PreferenceManager("")
    AppManager.RunApp(AppPref.Get("homeApp"))
