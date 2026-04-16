smallest = None
#print ('Before: ', smallest)
for num in [ 12, 24, 77, 22 , 3, 9, 10]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
   # print (num , smallest)
print ('After: ' , smallest)