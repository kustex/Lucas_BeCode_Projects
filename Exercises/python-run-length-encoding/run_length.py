import re

def encode(seq):
    index = 0
    result = ""
    while len(seq) != index:
        character = seq[index]
        match = re.findall(f"{character}+|$", seq[index:])[0]
        counter = len(match)
        if counter > 1:
            result += str(counter)
        result += character
        index += counter
    return result

def decode(seq):
    declist = re.findall("([0-9]*)?(.)", seq)
    result = ""
    for n in declist:
        if n[0] == '':
            result += n[1]
        else:
            result += (int(n[0]) * n[1])
    return result
