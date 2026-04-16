#відкрити файл notes.txt
#через for прогнати весь текст, і вивести тільки ті де є python
#порахувати та вивести в кінці Знайдено рядків (число)
count = 0
fhand = open('notes.txt', 'r')
for line in fhand:
    line = line.strip()
    if 'python' not in line.lower():
        continue
    count = count + 1
    print(line)

print('Count is:', count)