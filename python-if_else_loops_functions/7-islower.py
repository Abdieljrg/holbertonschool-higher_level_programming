#!/usr/bin/python3
def islower(c):
    mayusculas = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    minusculas = 'qwertyuiopasdfghjklzxcvbnm'
    if c in minusculas:
        return True
    else:
        return False
