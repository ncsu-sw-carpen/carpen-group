import re, csv, pdb

## open debugging, move this chunk around as needed
#pdb.set_trace()

## csv of experimental data
dataFile = 'data/swc.chemA.csv'
filehandle = open(dataFile)

## read the csv into a dictionary-like object
## see https://docs.python.org/2/library/csv.html
geneExpr = csv.DictReader(filehandle)

#for row in geneExpr:
#	print(row)

## look at one line
row01 = geneExpr.__next__() ## .next() did not work. Python 3 thing?
print ('\nData columns: ')
print (row01.keys())
print ('\nData values: ')
print (row01.values())
print ('\nPrinting gene value: ' + row01['gene'])

## We can access values using a named variable 
colName = 'Annotation'
## this is "fancy" string formatting in python
print ('Row01 has value %s for column %s\n' % (row01[colName], colName) )

## try to put "hard-coded" values in named variables
nlim = 5
ii = 0
print ("Printing %d rows of %s" % (nlim, colName))
## for each row 
for thisRow in geneExpr:
    print (thisRow[colName])
    ii += 1
    if (ii > nlim ): 
        ## exit the for loop
        break

input('\nHit enter to continue\n') ## In Python 2 this was raw_input
parenPatt = '\((\w+)\)'
ii = 0
colspace="\t"
linepattern="%d" + colspace + "%s" + colspace + "%s"
print ("Row", colspace, "group(0)", colspace, "group(1)")
for thisRow in geneExpr:
    ii += 1
    ## search for, e.g. 2015-01-01 00:00:01
    gene = re.search(parenPatt, thisRow['Annotation'])
    ## if there's *any* match
    if (gene):
        #print line
        ## print the pattern in the second group of parens 
        print (linepattern % (ii, gene.group(0), gene.group(1)))
