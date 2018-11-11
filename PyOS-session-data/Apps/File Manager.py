import os
homeDir = os.getcwd() + "/PyOS-session-data/Apps/filehome/"
fdir = homeDir

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
    shortDir = fdir.replace(homeDir, "~/")
    print("\033c")
    print(bcolors.FAIL + "|----------------- PyOS FileManager ------------------------------- |" + bcolors.ENDC)
    print(bcolors.FAIL + "| DIR: " + shortDir + "  VER: 1.0                          " + bcolors.ENDC)
    print(bcolors.FAIL + "| ----------------------------------------------------------------- |" + bcolors.ENDC)
    for file in os.scandir(fdir):
        line = ''
        if file.is_file():
            line += bcolors.WARNING + 'f'
        elif file.is_dir():
            line += bcolors.OKBLUE + 'd'
        elif file.is_symlink():
            line += bcolors.OKGREEN + 'l'
        line += '\t' + bcolors.ENDC
        print("{}{}".format(line, file.name))
    InputFile = input("Explore [Dir 'dir/']: ")

    if InputFile == "<HOMEDIR":
        fdir = homeDir
    elif "." in InputFile:
        FileOpen = open(fdir + InputFile, "r")
        os.system("clear")
        print(bcolors.FAIL + "|----------------- PyOS FileManager ------------------------------- |" + bcolors.ENDC)
        print(bcolors.FAIL + "| FILE: " + shortDir + InputFile + " M: TEDIT " + bcolors.ENDC)
        print(bcolors.FAIL + "| ----------------------------------------------------------------- |" + bcolors.ENDC)
        print(FileOpen.read())
        input("[ Click Enter to Exit ]")
    else:
        fdir = fdir + InputFile
