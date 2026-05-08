
# In Tuples this seems like in a list, here we have also index which also starts from zero


x = ('Glenn', 'Sally', 'Joseph') # constanta
# print(x[2])
y = ( 1, 9, 2 )
# print(max(y))
# for iter in y: print(iter)

# y[2] = 10    === Traceback
# but, they are immutable, so you can't just change it like in list
# no .sort() , no .append() , no .reverse()

l = list()
# print(dir(l), 'and')
t = tuple()
# print(dir(t))
# quick remaind: dir() show us what command we can use

( a , b ) = ( 6 , 'Frog' )# just like two assignment statements 
# print(b)
( q , w ) = ( 72 , 31 )
# print(q)
# and we can also use a return function to this tuples

d = dict()
d['cwen'] = 4
d['csev'] = 2
# for k,v in d.items() :
    # print(k,v)
tups = d.items()
# print(tups)

# ( 0, 1, 2 ) < ( 5, 1, 2 ) # the tuples also can be comparable, but its checked from first item, 
# if the first equal we go next, but if the next is not its finished to comparing
# ( 'Jones' , 'Sally') < ('Jones' , 'Sam') 

