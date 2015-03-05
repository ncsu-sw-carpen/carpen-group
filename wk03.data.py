import re, csv, pdb

## csv of experimental data
dataFile = 'data/swc.chemA.csv'
filehandle = open(dataFile)

## open debugging, move this chunk around as needed
pdb.set_trace()

## read the csv into a dictionary-like object
## see https://docs.python.org/2/library/csv.html
geneExpr = csv.DictReader(filehandle)

## look at one line
row01 = geneExpr.next()
print '\nData columns: ' 
print row01.keys()
print '\nData values: ' 
print row01.values()
print '\nPrinting gene value: ' + row01['gene']

## We can access values using a named variable 
colName = 'Annotation'
## this is "fancy" string formatting in python
print 'Row01 has value %s for column %s\n' % (row01[colName], colName) 

## try to put "hard-coded" values in named variables
nlim = 5
ii = 0
print "Printing %d rows of %s" % (nlim, colName)
## for each row 
for thisRow in geneExpr:
    print thisRow[colName]
    ii += 1
    if (ii > nlim ): 
        ## exit the for loop
        break

raw_input('\nHit enter to continue\n')
parenPatt = '\((\w+)\)'
ii = 0
print "Row\t\tgroup(0)\t\tgroup(1)"
for thisRow in geneExpr:
    ii += 1
    ## search for, e.g. 2015-01-01 00:00:01
    gene = re.search(parenPatt, thisRow['Annotation'])
    ## if there's *any* match
    if (gene):
        #print line
        ## print the pattern in the second group of parens 
        print "%d\t\t%s\t\t%s" % ( ii, gene.group(0), gene.group(1))
