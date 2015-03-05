import re

wikiDir = "carpen-group.wiki/ "
dataFile = "HW02.md"
fullname = wikiDir + dataFile
print fullname
f = open(fullname)
print f

## for each line of file
for line in f:
<<<<<<< HEAD
    ##print line
=======
    #print line
>>>>>>> fc47203dc06467882425a0b651f60491f3aebef5
    ## search for, e.g. 2015-01-01 00:00:01
    dateline = re.search('(\d+-\d+-\d+) (\d+:\d+:\d+).*', line)
    ## if there's *any* match
    if (dateline):
        #print line
        ## print the pattern in the second group of parens 
        print dateline.group(2)
