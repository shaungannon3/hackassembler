import re
# determines if line from assembly file contains code to be parsed
def is_code(line):
    if line != "\n" and re.search("^[\s/]+/.*", line, flags = re.S) == None:
        return True
    else:
        return False
