# list to a dictionary for count, then in list of tuples and sort by count and print top 3


list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'cherry', 'banana']

counts = dict()

for line in list:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# print(counts)

t = []
for k, v in counts.items():
    result = (v, k)
    t.append(result)


print( sorted (t[:3], reverse = True)  )