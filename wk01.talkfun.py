#!/usr/bin/python2
## Comments are lines starting with #
## except the very first line, which is special

def talk(say="Hello", to="World", sep=", "):
    '''## This is the docstring of function talk. \n## This function takes 3 arguments: say (string), to (string), sep (string) .'''
    retVar = say + sep + to
    return retVar

print(talk())

## extra stuff for later
#print dir(talk)
#print talk.__doc__
