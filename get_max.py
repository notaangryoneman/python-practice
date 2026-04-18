
def get_max(numbers):
    x = 0
    for n in numbers:
        if n > x:
            x = n
    return x

print(get_max([3, 7, 1, 9, 4]))
