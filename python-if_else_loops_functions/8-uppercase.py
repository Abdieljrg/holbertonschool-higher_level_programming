#!/usr/bin/python3
def islower(c):
    mayusculas = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    if c == "":
        raise Exception
    if c in mayusculas:
        return True
    else:
        return False
