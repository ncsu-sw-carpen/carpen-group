#!/usr/bin/python2
## Comments are lines starting with #
## except the very first line, which is special

def talk(say="Hello", to="World"):
    '''This is a docstring'''
    retVar = say + to
    return retVar

print talk()
print dir(talk)
