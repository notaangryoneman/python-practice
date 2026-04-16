inp1=input('Enter Per hour: ')
ph=float(inp1)
inp2=input('Enter Hours: ')
hrs=int(inp2)
nalog=1.41
cgp=float(ph*hrs/nalog)
print('Your netto pay is:',cgp,'You payed tax 41%')