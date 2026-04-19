def is_palindrome(text):
    result = ''
    for letter in text:
        result = letter + result 
    # return result
    if result == text:
        return True
    else:
        return False

print(is_palindrome('racecar'))