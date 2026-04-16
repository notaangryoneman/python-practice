#приймає рядок і вертає статистику доки не стане стоп
#першим видає довжину слова через len
#потім очищену версію без пробілів по бокам і всі маленькими літерами
#перевіряє чи є слово python в речені і ставить true false
#перший символ принтує
#другий символ принтує

def analyze(text):
    ltext = len(text) 
    return(ltext)
def clean(text):
    ctext = text.strip()
    return(ctext.lower()) 

while True:
    text = input('Enter text, and I will analyze: ')

    if text.lower() =='stop':
        break

    print('Довжина:', analyze(text))
    print('Очищено:', clean(text))
    found = 'python' in text.lower()
    print('Містить python:', found)
    print(text[0])
    print(text[-1])


