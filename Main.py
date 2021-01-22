#!python
from Parser import Parser
from Code import Code
from Symbol import Symbol
from Helper import is_code
import sys
import re
import Globals

def main(*args):
    Globals.initialize() # initialize global variables (symbol table)
    inputFile = str(sys.argv[1])
    outputFile = inputFile[:(len(inputFile) - 4)] + ".hack"

    # first pass through file to add labels to symbol table
    lineNumber = -1
    with open(inputFile, "r") as r:
        for line in r:
            if is_code(line):
                try: 
                    # if line contains label, add label to symbol table
                    label = re.findall("(?<=^\()\S*(?=\))", line)[0] 
                    Globals.symbolTable.add_label(label, lineNumber + 1) 
                except:
                    lineNumber += 1

    # second pass through file to parse lines with instructions
    lineNumber = -1
    with open(inputFile, "r") as r, open(outputFile, "w") as w:
        for line in r:
            if is_code(line):
                try: 
                    # pass if line contains label
                    re.findall("(?<=^\()\S*(?=\))", line)[0] 
                    pass
                except: 
                    # parse line into binary
                    lineNumber += 1
                    line = line.replace('\n','')
                    line = "".join(line.split(" "))
                    instruction = Parser(line)
                    instruction.parse()
                    code = Code(instruction)
                    code.translate()
                    w.write(code.get_binary() + '\n')
            else:
                pass

if __name__ == "__main__":
    main()
    
        

