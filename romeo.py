fname = input('Enter a file name: ')
fhand = open(fname)
lst = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)


lst.sort()
print(lst)