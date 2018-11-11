######################
#Legacy App Support
#
#Module for PyOS
######################

import os

def runlegacyapp(legappname):
    os.system("python2 " + os.getcwd() + "/LegacySupport/" + legappname)
