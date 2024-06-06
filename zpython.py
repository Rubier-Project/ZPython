from ZPy.console import ZConsole
from ZPy.executer import CanyouReadMe
from ZPy.executer import ImTierd
import sys

stat = {
    "msg": ">>> "
}

shCommands = [
    'pwd',

]

homePath = ZConsole.getPwd()
username = ZConsole.getUsername(ZConsole.getRandint())

def ZPython():
    while 1:
        user = str(ZConsole.getPrompt(stat['msg'].replace("@pwd", ZConsole.getPwd()).replace("@time", ZConsole.getTime()).replace("@user", username)))
        if user == "run":
            CanyouReadMe.getOutPut()

        elif user.startswith("$ps"):
            if user.replace("$ps ", "") != "$ps" or user.replace("$ps ", "") != " ":
                stat["msg"] = user.replace("$ps ", "")
            else:
                ZConsole.getPrompt(stat['msg'])

        elif user.startswith("ls"):
            pt = user.replace("ls ", "")
            if pt != "ls":
                ZConsole.getPathDir(user.replace("ls ", ""))
            else:
                ZConsole.getDir()

        elif user.startswith("dir"):
            pt = user.replace("dir ", "")
            if pt != "dir":
                ZConsole.getPathDir(user.replace("dir ", ""))
            else:
                ZConsole.getDir()

        elif user.startswith("cd"):
            pt = user.replace("cd ", "")
            if pt == "cd" or pt == "~" or pt == "home" or pt == " " or pt == "":
                ZConsole.changeDir(homePath)
            else:
                ZConsole.changeDir(pt)

        elif user == "cls" or user == "clear":
            ZConsole.clearConsole()

        elif user == "exit":
            sys.exit(0)

        else:
            ImTierd.addSource(user)

if __name__ == "__main__":
    try:
        ZPython()
    except KeyboardInterrupt:
        sys.exit(0)