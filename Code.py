# Takes parsed instruction and translates into binary
class Code():
    def __init__(self, instruction):
        self.instruction = instruction

    def translate(self):
        if self.instruction.get_type() == "a":
            self.binary = self.a_instruction()
        else:
            # create dictionaries of integers (converted to binary in c_instruction) associated with assembly codes
            self.comp_dict = {'0': 42, '1': 63, '-1': 58, 'D': 12, 'A': 48, 'M': 112, 
            '!D': 13, '!A': 49, '!M' : 113, '-D': 15, '-A': 51, '-M': 115, 'D+1': 31, 
            'A+1' : 55, 'M+1': 119, 'D-1': 14, 'A-1': 50, 'M-1': 114, 'D+A': 2, 
            'D+M' : 66, 'D-A': 19, 'D-M': 83, 'A-D': 7, 'M-D': 71, 'D&A': 0, 
            'D&M': 64, 'D|A': 21, 'D|M': 85}
            self.dest_dict = {'M': 1, 'D': 2, 'MD': 3, 'A': 4, 'AM': 5, 'AD': 6, 'AMD': 7}
            self.jump_dict = {'JGT': 1, 'JEQ': 2, 'JGE': 3, 'JLT': 4, 'JNE': 5, 'JLE': 6, 'JMP': 7}
            self.binary = self.c_instruction()

    def a_instruction(self):
        if self.instruction.get_address() != "":
            return '0' + '{0:015b}'.format(self.instruction.get_address())

    def c_instruction(self):
        return ('111' + '{0:07b}'.format(self.comp_dict[self.instruction.get_comp()])  + 
        '{0:03b}'.format(0 if self.instruction.get_dest() == "" else self.dest_dict[self.instruction.get_dest()]) + 
        '{0:03b}'.format(0 if self.instruction.get_jump() == "" else self.jump_dict[self.instruction.get_jump()]))

    def get_binary(self):
        return self.binary