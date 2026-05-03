text = 'python programming is awesome'

dict = {}
for letter in text:
    dict[letter] = dict.get(letter,0) + 1

res = max( dict, key = dict.get)
print( res , dict[res])