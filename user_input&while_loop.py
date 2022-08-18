'''
the input() function pauses your program and waits for the user to enter some text.
once python receives the user's input, it assigns that input to a variable to make it convenient for you to work with
'''

# mesage = input("what is ur name: ")
# print(mesage)

# use input(), python interprets everything the user enters as a string
# when you try to use the input to do a numerical camparision , you can ue int() to convert the string input to number

# age = input("how old are you")
# age = int(age)


'''
while loop
while True -> it is a flag means the program should run only aas long as many conditionss are true
'''
active = True

count = 0

while active:
    answer = 0
    answer = count + 1
    count += 1
    if answer == 10:
        active = False
    else:
        print(answer)

# using break to exit a loop.
print( " --------------------------")
'''
while True:
    city = input("start typing ")
    if city == 'q':
        break
    else:
        print(f"id love to go to {city.title()}")
'''
#

# use the continue statement to return to the beginning of the loop based on the result of a conditional test
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)
print("--------------------")
'''
while loop with list & dictionaries
'''

list1 = ['a', 'b', 'c', 'd']
list2 = []

while list1:    # run as long as list1 is not empty
    v = list1.pop()

    list2.append(v)

print(list2)

print("//////////////////////////////")
# removing all instances of specific values from a list
num = [1,2,4,6,87,2,4,5,6,2]
print(num)
while 2 in num:
    num.remove(2)


print(sorted(num))


