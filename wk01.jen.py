#!/usr/bin/python2
## Comments are lines starting with #
## except the very first line, which is special

def talk(say="Hello", to="World", sep=", "):
    '''## This is the docstring of function talk. \n## This function takes 3 arguments: say (string), to (string), sep (string) .'''
    ## in R, this would be c(say, sep, to) 
    retVar = say + sep + to
    return retVar

print talk(say="Goodbye Cruel", sep=" ")
=======
talk(say="Goodbye cruel", sep=" ")
>>>>>>> ae410738f969327c81a228dfd60a2c5c4b984280

## extra stuff for later
#print dir(talk)
#print talk.__doc__
