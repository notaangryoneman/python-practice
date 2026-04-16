#це перевірка пароля
#це циклічно із виводом одразу поки нема exit 
#функція check_lenght(password) довжина вертає True якщо >=8
#функція check_digit(password) цифра вертає True якщо є цифра але треба пройтись з for по password і перевірити через char.isdigit()
#streng повертає слабкий якщо нема умов середній якщо одна є та сильний якщо є обидві
def check_lenght(password):
    lenght = False
    if len(password) >=8 :
        lenght = True
    return(lenght)

def check_digit(password):
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    return(has_digit)
while True:
    streng = 0
    password = input('Enter password: ')
    if password.lower =='exit':
        break
    print('Long enought', check_lenght(password))
    print('Has numbers', check_digit(password))
    if check_lenght(password) == True:
        streng = streng + 1
    elif check_digit(password) == True:
        streng = streng + 1
    if streng  == 2 :
        print('password is strong')
    elif streng == 1 :
        print('password is middle')
    else:
        print('password is weak')