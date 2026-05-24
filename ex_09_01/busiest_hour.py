# open and run thru the file using .startwith('From:') 
# extract the email and hour and build a dictionary where key=hour and value=email_counts 
# print the busiest hour

print('Enter file name: ')
fname = input('-')
if len (fname) < 1 : fname = 'mbox-short.txt'

hours = dict()

fhand = open(fname)

for line in fhand:
    line = line.strip()
    if not line.startswith('From ') : continue
    # print(line)
    words = line.split()
    email = words[1]
    hour = words[5]
    hour = hour.split(':')
    hour = hour[0]

    if not hour in hours : 
        hours[hour] = 1
    else: hours[hour] = hours[hour] + 1

    # for key, val in emails:
    #     print(key, val)
print(max(hours , key = hours.get))