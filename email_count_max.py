file = input('Enter file name: ')
if len(file) < 1:
    file = 'mbox-short.txt'

counts = 0
emails = dict()

fhand = open(file)
#need to add emails and their count to a dicttionary, and show from who we have a most of lists
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split() 
    email = words[1]
    if not email in emails:
        emails[email] = 1
    else: emails[email] = emails[email] + 1

best = max(emails, key = emails.get)
print(best, emails[best])

# print(counts)