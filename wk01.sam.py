#!/usr/bin/python2
## Comments are lines starting with #
## except the very first line, which is special

def talk(say="Hello", to="world", sep=", "):
    '''## This is the docstring of function talk. \n## This function takes 3 arguments: say (string), to (string), sep (string) .'''
<<<<<<< HEAD:wk01.sam.py
    ## in R, this would be c(say, sep, to)
    retVar = say + sep + to
    return retVar

print talk(say="goodbye cruel", sep=" ")
=======
<<<<<<< HEAD
    ## In R, this would be c(say, sep, to)
    retVar = say + sep + to
    return retVar

print talk(say = "Goodbye, cruel", sep = " ")
=======
    ## in R, this would be c(say, sep, to) 
    retVar = say + sep + to
    return retVar

talk(say="Goodbye cruel", sep=" ")
>>>>>>> ae410738f969327c81a228dfd60a2c5c4b984280
>>>>>>> f1c0d05f1c167981d897b08b1e806f1f17d6e6a4:wk01.talkfun.py

## extra stuff for later
#print dir(talk)
#print talk.__doc__
