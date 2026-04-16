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