largest = None
smallest = None
count = 0
total = 0
while True: 
    rating = input('Enter score or done: ')
    if rating == 'done':
        break

    try: 
        fr = float(rating)
    except:
        print('Enter numbers only')
        continue 

    if fr < 0 or fr > 100:
        print('Enter a number between 0 and 100')
        continue

    count = count + 1
    total = total + fr

    if largest is None or fr > largest:
        largest = fr   
        
    if smallest is None or fr < smallest:
        smallest = fr
    
    if fr < 60:
        print('Your score is F ')
    elif fr < 70:
        print('Your score is D ')  
    elif fr < 80:
        print('Your score is C ')  
    elif fr < 90:
        print('Your score is B ')
    elif fr < 101:
        print('Your score is A ')

print('Count is' , count)
print('Total is' , total)
print('Average is' , total / count)
print('Largest is' , largest)
print('Smallest is' , smallest)