words = dict()

while True:
    print('Enter words ')
    inp = input('')
    if inp.lower() == 'done':
        break
    if not inp in words:
        words[inp] = 1
    else: words[inp] = words[inp] + 1

print(words)
