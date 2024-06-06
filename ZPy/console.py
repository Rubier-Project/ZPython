from prompt_toolkit import prompt
from typing import Callable
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text.base import StyleAndTextTuples
import prompt_toolkit.lexers
import re
import rich
import time
import random
import hashlib
import os

class ZPythonLexer(prompt_toolkit.lexers.Lexer):
    def __init__(self, regex_mapping):
        super().__init__()
        self.regex_mapping = regex_mapping

    def lex_document(self, document: Document) -> Callable[[int], StyleAndTextTuples]:
        def lex(_: int):
            line = document.text
            tokens = []
            while len(line) != 0:
                for pattern, style_string in self.regex_mapping.items():
                    match: re.Match = pattern.search(line)

                    if not match:
                        continue
                    else:
                        pass
                    match_string = line[:match.span()[1]]
                    line = line[match.span()[1]:]
                    tokens.append((style_string, match_string))
                    break
            return tokens
        return lex

# Special words -> GREEN, YELLOW, ORANGE, CYAN
numbers = re.compile(r"^\d+(\.\d+)?")
text = re.compile(r"^.")
operators = re.compile(r'^[+*/<>=?]{1,2}')
dobuleDash = re.compile(r"^--[a-zA-Z_]*")
oneDash = re.compile(r'^-[a-zA-Z_]*')
cout = re.compile(r'^"(.*?)"')
ocout = re.compile(r"^'(.*?)'")
op = re.compile(r"^[(]")
ox = re.compile(r"^[)]")

# Keywords -> RED
importer = re.compile("^import")
fromTime = re.compile("^from")
classTime = re.compile("^class")
funcTime = re.compile("^def")
delTime = re.compile("^del")
ifTime = re.compile("^if")
elifTime = re.compile("^elif")
elseTime = re.compile("^else")
tryTime = re.compile("^try")
exceptTime = re.compile("^except")
whileTime = re.compile("^while")
withTime = re.compile("^with")
yieldTime = re.compile("^yield")
raiser = re.compile("^raise")
returner = re.compile("^return")
is_ = re.compile("^is")
in_ = re.compile("^in")
or_ = re.compile("^or")
as_ = re.compile("^as")
pass_ = re.compile("^pass")
assert_ = re.compile("^assert")
and_ = re.compile("^and")
async_ = re.compile("^async")
await_ = re.compile("^await")
finally_ = re.compile("^finally")
for_ = re.compile("^for")
global_ = re.compile("^global")
lambda_ = re.compile("^lambda")
case_ = re.compile("^case")
continue_ = re.compile("^countinue")
break_ = re.compile("^break")
nonlocal_ = re.compile("^nonlocal")
not_ = re.compile("^not")
match_ = re.compile("^match")

# Functions -> PURPLE
printer = re.compile("^print")
power = re.compile("^pow")
tupler = re.compile("^tuple")
lister = re.compile("^list")
dicter = re.compile("^dict")
string = re.compile("^str")
integer = re.compile("^int")
seter = re.compile("^set")

regex_mapping = eval(open("ZPy/theme.json", 'r').read())

ZPyLexer = ZPythonLexer(regex_mapping)

class ZMessagePrompt(object):
    def classic():
        return ">>> "
    
    def python_message():
        return "python>>> "

class ZConsole(object):
    def getPrompt(message: str = ZMessagePrompt.classic()):
        return prompt(message=message, lexer=ZPyLexer)
    
    def clearConsole():
        os.system("cls || clear")

    def getDir():
        os.system("ls || dir")

    def getPathDir(path: str):
        if os.path.exists(path):
            if os.path.isdir(path):
                print(rich.print(os.listdir(path)))
            else:
                print("Path is not a dir")
        else:
            print("Path does not exists")

    def getPwd():
        return os.getcwd()
    
    def getTime():
        return time.strftime("%H:%M:%S")
    
    def changeDir(path: str):
        if os.path.exists(path):
            if os.path.isdir(path):
                os.chdir(path)
            else:
                print("Path is not a dir")
        else:
            print("Path does not exists")

    def getUsername(inp: str):
        md5 = hashlib.md5()
        md5.update(inp.encode())
        return md5.hexdigest()
    
    def getRandint():
        return str(random.randint(0, 100))