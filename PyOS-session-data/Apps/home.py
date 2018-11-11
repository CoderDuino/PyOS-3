#########################
# Simple Home Screen For PyOS3
# By: Ari Stehney
# Simple Text Homescreen
#########################

import AppManager
import sys
import TerminalGui as gui

while True:
    gui.clear()
    
    gui.tprint(gui.formatCodes.OKBLUE, "████████ Home Screen █████████████")
    gui.tprint(gui.formatCodes.FAIL, "█                                █  ")
    gui.tprint(gui.formatCodes.FAIL, "█  #Test.py#          #File.py#  █  ")
    gui.tprint(gui.formatCodes.FAIL, "█  ##HI ...#          ##File ##  █  ")
    gui.tprint(gui.formatCodes.FAIL, "█  # [RUN] #          # [RUN] #  █  ")
    gui.tprint(gui.formatCodes.FAIL, "█                                █  ")
    gui.tprint(gui.formatCodes.OKGREEN, "█ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ █ ")
    gui.tprint(gui.formatCodes.FAIL, "█                                █  ")
    gui.tprint(gui.formatCodes.FAIL, "█  #Term.py#          #Stop.py#  █  ")
    gui.tprint(gui.formatCodes.FAIL, "█  ##H@H $ #          ##>>S<<##  █  ")
    gui.tprint(gui.formatCodes.FAIL, "█  # [RUN] #          # [RUN] #  █  ")
    gui.tprint(gui.formatCodes.FAIL, "█                                █  ")
    gui.tprint(gui.formatCodes.FAIL, "█  OR TYPE OTHER FILE NAME       █ ")
    gui.tprint(gui.formatCodes.OKBLUE, "██████████████████████████████████")
    
    Opt = input("")
    if Opt == "quit":
        sys.exit()

    AppManager.RunApp(Opt)