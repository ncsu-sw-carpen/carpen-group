import csv
filehandle=open('data/swc.chemA.csv')
reader = csv.DictReader(filehandle)
for row in reader:
    print(row['test_id'], row['gene'])
