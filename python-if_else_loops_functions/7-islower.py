#!/usr/bin/python3
def islower(c):
    minusculas = 'qwertyuiopasdfghjklzxcvbnm'
    if c == "":
        raise Exception
    if c in minusculas:
        return True
    else:
        return False
