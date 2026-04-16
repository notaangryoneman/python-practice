#заведення функції bmi
def bmi (height , weight): 
    try:
        h = float(height)
    except:
        return('Enter numbers ')#return для повернення функції
    try:
        w = float(weight)
    except:
        return('Enter numbers ')
    bmi_value = w / ( h **2)
    return(bmi_value)
    
def category(bmi_value ):
    if bmi_value < 18.5:
        return('Too small')
    elif bmi_value < 25:
        return('Normal')
    elif bmi_value >= 25:
        return('Too much')
        
while True:
    raw = input('Weight: ' or 'stop' ) 
    if raw =='stop':
        break
    
    height = input('Height: ')
    
    result = bmi (height , raw) #виклик функції
    print(result) #вивод bmi
    print(category(result)) #вивод результату
    ask = input('stop or again? ')
    if ask =='stop':
        print('Bye!')
        break 