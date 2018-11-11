########################
# Videos App
# By: Ari Stehney
# For PyOS3.6
########################
import time
import AppManager
import os
import sys
import TerminalGui as gui
gui.clear()
gui.tprint(gui.formatCodes.OKBLUE, "████████ Videos ██████████████████")
gui.tprint(gui.formatCodes.FAIL, "█                                █  ")
gui.tprint(gui.formatCodes.FAIL, "█  Type Video Name               █  ")
gui.tprint(gui.formatCodes.FAIL, "█                                █  ")
gui.tprint(gui.formatCodes.OKBLUE, "██████████████████████████████████")

Opt = input("")
os.system("mplayer " + Opt);
  
