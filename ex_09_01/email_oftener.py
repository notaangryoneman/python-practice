#find the spammer 
#open mbox-short and extract email and hour with .startwith('From ')
#make it in list of tuples(email , hour)
#find which (email , hour) combination appears most oftener

counts = dict()
t = list()
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.strip()
    if not line.startswith('From ') : continue
    # print(line)
    words = line.split()
    email = words[1]
    hour = words[5]
    hour = hour.split(':')
    hour = hour[0]
    combination = (email, hour)
    t.append(combination)

for item in t:
    counts[item] = counts.get(item , 0) + 1

print(max(counts , key = counts.get))