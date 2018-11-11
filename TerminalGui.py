class formatCodes:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def tprint(Style, Text, end="\n"):
    print(Style + Text + "\033[0m", end=end)
    
def clear():
    print("\033c", end="")

def drawDialog(Title, Message, Width=30):
    def drawLine():
        print(formatCodes.FAIL + "|" + "-" * (Width - 2) + "|" + formatCodes.ENDC)

    def printCenter(Line, WidthOffset=0):
        print(formatCodes.FAIL + "|", end="")

        Spaces = Width - len(Line) - 2 + WidthOffset
        HalfSpaces = int(Spaces / 2)

        if HalfSpaces * 2 == Spaces:
            print(" " * HalfSpaces, end="")
        else:
            print(" " * (HalfSpaces + 1), end="")

        print(Line + " " * HalfSpaces + "|" + formatCodes.ENDC)

    if "\n" in Title or len(Title) > Width - 4:
        raise ValueError("Title To Long Or Contains Illegal Characters!")

    clear()
    drawLine()
    printCenter(Title.upper())
    printCenter("")
    printCenter("")

    for line in Message.split("\n"):
        printCenter(line[:Width - 4])

    printCenter("")
    printCenter(formatCodes.OKGREEN + "[ OK ]" + formatCodes.ENDC + formatCodes.FAIL, WidthOffset=14)
    drawLine()

    input("")
    clear()