import re
import Globals

class Parser():
    def __init__(self, instruction):
        self.instruction = re.split("/", instruction)[0]
        self.type = "a" if instruction.find("@") == 0 else "c"
        self.address = ""
        self.dest = ""
        self.comp = ""
        self.jmp = ""

    def parse(self):
        if self.type == "a":
            try:
                variable = re.findall("(?<=^@)([^0-9]\S*)", self.instruction)[0]
                Globals.symbolTable.add_variable(variable)
                self.address = Globals.symbolTable[variable]
            except:
                self.address = int(self.instruction[1:])         
        elif self.type == "c":
            instructionCopy = self.instruction
            jmp = self.instruction.find(";")
            if jmp != -1:
                self.jmp = self.instruction[jmp+1:]
                instructionCopy = instructionCopy[:jmp]
            dest = self.instruction.find("=")
            if dest != -1:
                self.dest = self.instruction[:dest]
                instructionCopy = instructionCopy[dest+1:]
            self.comp = instructionCopy

    def get_type(self):
        return self.type
    
    def get_address(self):
        return self.address
    
    def get_jump(self):
        return self.jmp
    
    def get_dest(self):
        return self.dest
    
    def get_comp(self):
        return self.comp