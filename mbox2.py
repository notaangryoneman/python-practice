file = input('Enter file name: ')
if len(file) < 1:
    file = 'mbox-short.txt'

count = 0

fhand = open(file)

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    count = count + 1
    words = line.split() 
    email = words[1]
    print(email)
print("There were", count, "lines in the file with From as the first word")
