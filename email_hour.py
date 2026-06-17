
counts = dict()

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)

# using find method to line.startwith('From') find a hour when messages was sended, using colon extract a hours
# count them and use .sort by a hour 

for line in fhandle :
    line = line.strip()
    if not line.startswith('From') : continue
    #for words in line:  тут не потрібний 
    words = line.split()
    # print(words)
    if len(words) < 5 : continue
    time_str = words[5]
    time = time_str.split(':')
    # print(time)
    hours = time[0]
    # print(hours)
    counts[hours] = counts.get( hours , 0 ) + 1
        
# print( sorted( [ (k,v) for k,v in counts.items() ] ) )

for k,v in sorted(counts.items()) :
    print( k,v )