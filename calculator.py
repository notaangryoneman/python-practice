sr=input('Enter rate: ')
sh=input('Enter Hours: ')
fr=float(sr)
fh=float(sh)
#print(fr, fh)
if fh>40:
   # print('Overtime')
    reg=fr*fh
    otp = (fh - 40.0) * (fr * 0.5)
    x=reg+otp
else:
    #print('Regular')
    x=float(fh*fr)
print('Pay:',x)