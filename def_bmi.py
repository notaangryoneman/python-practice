
height = input ('How tall are you?')
weight = input ('How much do you weight?')

def bmi ( weight , height ):
    try:
         h = int(height)
    except:
     return ('Enter numbers')
    
    try:
         w = int( weight )
    except:
         return ('Enter numbers')
    bmiv = w / (h ** 2)

    return bmiv

bmi_value = bmi(weight, height)
if bmi_value < 18.5:
    print ('Too small')
elif bmi_value < 25:
    print ('Normal') 
elif bmi_value >= 25:
    print ('Too large')
