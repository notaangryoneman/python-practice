# # # # # # # # # # cards = list()
# # # # # # # # # # cards.append(12)
# # # # # # # # # # cards.append(3)
# # # # # # # # # # cards.append(75)
# # # # # # # # # # print(cards)
# # # # # # # # # # print(cards[1])
# # # # # # # # # # cards[1] = cards[1] + 2
# # # # # # # # # # print(cards)

# # # # # # # # # cabinet = dict()
# # # # # # # # # cabinet['summer'] = 12
# # # # # # # # # cabinet['fall'] = 3
# # # # # # # # # cabinet['spring'] = 75
# # # # # # # # # print(cabinet)
# # # # # # # # # print(cabinet['fall'])
# # # # # # # # # cabinet['fall'] = cabinet['fall'] + 2
# # # # # # # # # print(cabinet)

# # # # # # # # # lst = list()
# # # # # # # # # lst.append(21)
# # # # # # # # # lst.append(183)
# # # # # # # # # print(lst)
# # # # # # # # # lst[0] = 23
# # # # # # # # # print(lst)

# # # # # # # # # ddd = dict()
# # # # # # # # # ddd['age'] = 21
# # # # # # # # # ddd['course'] = 182
# # # # # # # # # print(ddd)
# # # # # # # # # ddd['age'] = 23
# # # # # # # # # print(ddd)

# # # # # # # # jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
# # # # # # # # print(jjj)
# # # # # # # # print(jjj['chuck']) # для виклику ключа потрібні лапки ' '
# # # # # # # # ooo = {}
# # # # # # # # print(ooo)

# # # # # # # ccc = dict()
# # # # # # # ccc['csev'] = 1 
# # # # # # # ccc['cwen'] = 1
# # # # # # # print(ccc)
# # # # # # # ccc['cwen'] = ccc['cwen'] + 1
# # # # # # # print(ccc)

# # # # # # # # print(ccc['DDDDDD']) # this would make a Traceback, if we dont have a key in dictionaries its make boom for us
# # # # # # # if 'DDDDDD' in ccc:
# # # # # # #     print('True')
# # # # # # # else: print('False')


# # # # # # counts = dict()
# # # # # # names = ['csev' , 'cwen' , 'csev' , 'zqian' , 'cwen']
# # # # # # # for name in names:
# # # # # # #     if name not in counts:
# # # # # # #         counts[name] = 1
# # # # # # #     else:
# # # # # # #         counts[name] = counts[name] + 1


# # # # # # for name in names:
# # # # # #     counts[name] = counts.get(name , 0) + 1
# # # # # # print(counts)

# # # # # # # x = counts.get('csev', 0)
# # # # # # # print(x)



# # # # # counts = dict ()
# # # # # print('Enter a line of text: ')
# # # # # line = input('')

# # # # # words = line.split()

# # # # # print('Words: ', words)

# # # # # print('Counting...')
# # # # # for word in words:
# # # # #     counts[word] = counts.get(word,0) + 1
# # # # # print('Counts', counts)



# # # # counts = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
# # # # for key in counts:
# # # #     print(key, counts[key])



# # # jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
# # # print(list(jjj))
# # # print(list(jjj.keys()))
# # # print(list(jjj.values()))
# # # print(list(jjj.items())) # items get you a keys and they values, and in result you have something that called 'tuple'?


# # jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
# # for aaa,bbb in jjj.items() :
# #     print(aaa, bbb)


# name = input('Enter file: ')
# handle = open(name)

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)