#!/usr/bin/python2
## Comments are lines starting with #
## except the very first line, which is special

def talk(say="Hello", to="world", sep=", "):
    '''## This is the docstring of function talk. \n## This function takes 3 arguments: say (string), to (string), sep (string) .'''
    ## In R, this would be c(say, sep, to)
    retVar = say + sep + to
    return retVar

print talk(say = "Goodbye, cruel", sep = " ")

## extra stuff for later
#print dir(talk)
#print talk.__doc__
