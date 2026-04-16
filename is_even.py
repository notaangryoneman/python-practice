# def is_even(n):
#     return n % 2 == 0

# for i in range(1, 21):
#     if is_even(i):
#         print(i)



# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#     elif n % 5 == 0:
#         return 'Buzz'
#     elif n % 3 == 0:
#         return 'Fizz'
#     else:
#         return n 

# for i in range(1, 31):
#     print(fizzbuzz(i))


#створити пустий словник
#запитати текст
#розділити текст 
#прогнати текст через for і порахувати як часто слово повторяється записавши результат у словник
#відкрити словник 
#
#

def count_words(text):
    result = {}
    words = text.split()
    for word in words:
        if word in result:
            result[word] +=1
        else:
            result[word] = 1
    return result

text = input('Enter text: ')
print(count_words(text))