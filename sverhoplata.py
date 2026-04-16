askh=input('How much hour? ' )
h=int(askh)
askph=input('How much per hour ?' )
ph=float(askph)
if h<40:
    ph=ph*1
elif h>40:
    ph=(h-40)*1.5
pay=float(ph*h)
print(pay)
