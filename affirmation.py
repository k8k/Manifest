from sys import argv

script, filename = argv

openfile = open(filename)
text_of_file = openfile.read()
words = text_of_file.split().strip()
# print rows
# print type(rows)

# for row in text_of_file:
#     print row
#     print type(row)

wordcount_dict = {}

for item in words:
    if item in wordcount_dict:
        wordcount_dict[item] += 1
    else:
        wordcount_dict[item] = 1

for word, count in wordcount_dict.iteritems():
    print word, count
