sr=input('Enter rate: ')
sh=input('Enter Hours: ')
try:
    fr=float(sr)
    fh=float(sh)
except: 
     print('Error: enter numbers, not a letters! Or are programms only for smart people?') 
     exit()
#print(fr, fh)
if fh>40:
   # print('Overtime')
    reg=fr*fh
    otp = (fh - 40.0) * (fr * 0.5)
    x=reg+otp
elif fh>50:
    # print('double Overtime')
    reg=fr*fh
    otp = (fh - 50.0) * ((fr * 0.5)*2)
    x=reg+otp
else:
    #print('Regular')
    x=float(fh*fr)
print('Pay brutto:',x)
netto = input('Do you want to calculate netto? ')
if netto == 'No' or netto == 'no' or netto == 'NO':
    print('Pay brutto:',x)
elif netto == 'Yes' or netto == 'yes' or netto == 'YES':
    htax = input('Enter tax number : ')
    if htax == '1':
        tax1 = x * ( 1 - 42 / 100)
        print('Pay netto:', tax1 )
    elif htax == '2':
            tax2 = x * ( 1 - 15 / 100)
            print('Pay netto:', tax2 )
    elif htax == '3':
          tax3 = x * ( 1 - 90 / 100)
          print('Pay netto:', tax3 )