
# In Tuples this seems like in a list, here we have also index which also starts from zero


x = ('Glenn', 'Sally', 'Joseph') # constant
# print(x[2])
y = ( 1, 9, 2 )
# print(max(y))
# for iter in y: print(iter)

# y[2] = 10    === Traceback
# but, they are immutable, so you can't just change it like in list
# no .sort() , no .append() , no .reverse()

# l = list()
# print(dir(l), 'and')
# t = tuple()
# print(dir(t))
# quick remaind: dir() show us which of command we can use

# ( a , b ) = ( 6 , 'Frog' )# just like two assignment statements 
# print(b)
# ( q , w ) = ( 72 , 31 )
# print(q)
# and we can also use a return function to this tuples

# d = dict()
# d['cwen'] = 4
# d['csev'] = 2
# for k,v in d.items() :
    # print(k,v)
# tups = d.items()
# print(tups)

# ( 0, 1, 2 ) < ( 5, 1, 2 ) # the tuples also can be comparable, but its checked from first item, 
# if the first equal we go next, but if the next is not its finished to comparing
# ( 'Jones' , 'Sally') < ('Jones' , 'Sam') 


# tuple = {'a':10, 'c':22, 'b':1}
# print(tuple.items())
# print(sorted(tuple.items()))

d = {'a':10, 'c':22, 'b':1}
# t = sorted(d.items())
# print(t)
# for k,v in sorted(d.items()):
    # print(k,v)

# tmp = list()
# for k,v in d.items():
#     tmp.append( (v,k) )
#  print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)f

# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# #
# lst = list()
# for key, val in counts.items():
#     newtup = (val, key) 
#     lst.append(newtup)
# #
# lst = sorted(lst, reverse=True)
# #
# for val, key in lst[:10] :
#     print(key, val)

c = {'a':10, 'c':22, 'b':1}

# print( sorted( [ (v,k) for k,v in c.items() ] ) )