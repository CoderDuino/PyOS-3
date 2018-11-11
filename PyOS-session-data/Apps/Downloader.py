######################
#Internet App Installer
#
#Module for PyOS
######################

import AppManager
import time
import os
from PreferenceManager import PreferenceManager

MountLoc = os.getcwd()

print("\033c")
print("|---------------- Internet App Downloader -----------------|")
AddressD = input("| STEP1 | Download Address [http_://www._____.com/____]: ")
InstallNameF = input("| STEP2 | Install File Name: ")
InstallNameA = input("| STEP3 | Install Name: ")
input("| STEP5 | Click Enter to Install!")
os.system("curl -o " + MountLoc + "/PyOS-session-data/Apps/" + InstallNameF + " " + AddressD)
AppPref = PreferenceManager("Apps")
AppPref.Set(InstallNameF, InstallNameA)