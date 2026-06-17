# # x = 33
# # while x < 100:
# #     x = x + 20
# #     print(x)

# # count = 0
# # x = ( 1, 2, 3, 4, 7)
# # for n in x:
# #     count = count + 1
# # print(count)


# # height = input('How tall? ')
# # weight = input('How much kg have you? ')
# # def bmi ( height , weight ):
# #     try:
# #         h = float(height) / 100
# #     except:
# #         return('Only numbers ')
    
# #     try:
# #         w = float(weight)
# #     except:
# #         return('Only numbers ')
# #     bmi_res =  w / h ** 2
# #     return(bmi_res)

# # def category ( bmi_res):
# #     if bmi_res < 18.5 :
# #         return(' Більше їсти треба ')
# #     elif bmi_res < 25 :
# #         return(' Чіназес ')
# #     elif bmi_res >= 25 :
# #         return(' Пора підхуднути комусь ')

# # result = bmi(height , weight)
# # print(result)
# # print(category(result))

# # print(bmi( height , weight ))



# def total_pushups(workout):
#     total_pushups = 0
#     for workout in workouts:
#         x = workout['pushups']
#         total_pushups = total_pushups + x
#     return(total_pushups)



# def best_day(workouts): #return найкращий день по віджиманням
#     counts = dict()
#     for item in workouts:
#         counts[item['day']] = item['pushups']# ітерує workouts, будує словник {item: pushups}, повертає item з max
#     return(max(counts , key = counts.get))


# workouts = [
#     {"day": "Monday", "type": "A", "pushups": 40},
#     {"day": "Wednesday", "type": "B", "pushups": 0},
#     {"day": "Friday", "type": "A", "pushups": 55},
#     {"day": "Sunday", "type": "C", "pushups": 0},
# ]

# print('Totally: ' , total_pushups(workouts))
# print('And the best day is : ' , best_day(workouts))



#run thru the file looking 'From: ' line and take second word
#create a dict() that maps (key, value) and count them
# using max() to find most prolific commiter 


# print('Enter file name to read: ')
# file = input('File name: ')
# if len(file) < 1 :
#     file = 'mbox-short.txt'

# counts = dict()
# fhand = open(file) 

# for line in fhand:
#     line = line.strip()
#     if not line.startswith('From ') : continue 
#     # print(line)
#     words = line.split()
#     # print(words)
#     emails = words[1]
#     # print(emails)
#     counts[emails] = counts.get(emails , 0) + 1
#     # print(counts)
#     spammer = max(counts , key = counts.get)
#     spammer_times = counts[spammer]
# print('The oftener email is:', spammer,', and it was', spammer_times , 'times')


# age = ( 10 , 20 )
# name = ( 'Molly' , 'John' )

# name = age
# # print( name[0] )

# age = (99,100)
# print( name[0])