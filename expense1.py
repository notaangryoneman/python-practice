def categorize(amount):
    if amount < 20:
        return('This is a small operation, dont worry')
    elif amount < 100:
        return('This is a medium operation, its okay')
    elif amount >= 100:
        return('This is a large operation, not bad')

income = 0
income_count = 0
expenses = 0
expenses_count = 0

while True:
    print('1 - add income ')
    print('2 - add expense ')
    print('3 - show report ')
    print('4 - exit ')
    choice = input(' Enter number to choose: ')

    if choice == '4':
        break
    elif choice =='1':
        try:
            amount = float(input('Enter income amount: ')) 
        except:
            print('Enter only numbers')
            continue
        if amount < 0:
            print('Amount cannot be negative')
            continue
        income = income + amount 
        income_count = income_count + 1
        print(categorize(amount))
    elif choice =='2':
        try:
            amount = float(input('Enter expenses amount: ')) 
        except:
            print('Enter only numbers')
            continue
        if amount < 0:
            print('Amount cannot be negative')
            continue
        expenses = expenses + amount
        expenses_count = expenses_count + 1
        print(categorize(amount))
    elif choice =='3':
        print('Summary: ')
        print('Income: ' , income , income_count ,'transactions')
        print('Expenses: ', expenses , expenses_count ,'transactions')
        balance = income - expenses 
        print('Balance: ' , balance )
