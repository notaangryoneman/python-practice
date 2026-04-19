
# def reverse_string(text):
#     result = ''
#     for letter in text:
#         result = letter + result
#     return result

def reverse_string(text):
    result = []
    for letter in text:
        result.append(letter)#додає в кінець букви
    result.reverse()#перевертає результат
    return ''.join(result)# збирає в рядок букви і робить їх словом цілим 

print(reverse_string('hello'))