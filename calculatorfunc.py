def computepay( hours , rate) :
    #print('In computepay' , hours , rate)
    if hours >40:
        reg=rate*hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay=reg+otp
    else:
        pay = hours * rate   
    #print('Returning' , pay)
    return pay

sr=input('Enter rate: ')
sh=input('Enter Hours: ')
fr=float(sr)
fh=float(sh)

x=computepay(fh, fr)

print('Pay',x)