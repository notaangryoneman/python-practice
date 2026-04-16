# Use the file name mbox-short.txt as the file name
while True:
    fname = input("Enter file name: ")
    try:
        fn = open(fname)
        break 
    except FileNotFoundError:
        print('спробуй ще раз ')

# print(fn)  
count = 0
snumbers = 0
for line in fn:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    ftext = line.find(':')
    numbers_str = line[ftext + 1 :].strip()
    numbers = float( numbers_str )
    snumbers = snumbers + numbers
    medium = snumbers / count 
    # print(line)
    # print(numbers)
# print(snumbers)
print('Average spam confidence:', medium)