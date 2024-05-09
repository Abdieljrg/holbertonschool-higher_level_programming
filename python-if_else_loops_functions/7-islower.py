#!/usr/bin/python3
def islower(c):
    minusculas = 'qwertyuiopasdfghjklzxcvbnm'
    if not c:
        return False
    if c in minusculas:
        return True
    else:
        return False
