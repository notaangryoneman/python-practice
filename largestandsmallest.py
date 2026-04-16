largest = None
smallest = None
while True: 
    num = input('Enter a number: ')
    #print(num)
    if num == 'done':
        break

    try: 
        inum = int(num)
    except:
        print('Invalid input')
        continue
    #логіка для найбільшого числа
    if largest is None or inum > largest:
        largest = inum
    #логіка для найменшого числа
    if smallest is None or inum < smallest:
        smallest = inum
#print(largest , smallest)
print ('Maximum is', largest)
print ('Minimum is', smallest)
