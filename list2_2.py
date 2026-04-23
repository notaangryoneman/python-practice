abc = 'With three words'
stuff = abc.split()
# print(stuff)
# print(len(stuff))
# # print(stuff[0])
# for w in stuff :
#     print(w)

line = 'With;three;words'
# thing = line.split() # в дужках вказуємо що робити з пробелами між словами
# print(thing) # буде рахуватись як одне число через ;
# print(len(thing))
thing = line.split(';') # вписувати без пробела
# print(thing)
# print(len(thing))

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From') : continue
    words = line.split() 
    # print(words[1])
    email = words[1] # split в середині другого split 
    pieces = email.split('@') # а це вже split в split в третьому split
    print(pieces)
     