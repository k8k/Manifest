from sys import argv
from string import digits

script, filename = argv

openfile = open(filename)
text_of_file = openfile.read()
rows = text_of_file.split("\n")

clean_rows=[]

for row in rows:
    clean_row=row.translate(None,digits)
    clean_row=clean_row.lstrip(". ")
    clean_rows.append(clean_row)


print clean_rows
