'''
for loop
'''

arr = ['alice', 'david', 'carolina', 'marry', 'justin']
for i in arr:
    print(f"{i.title()}, is a good name")
    #print(i)


#any lines of code after the for loop that are not indentted are executed once without repetition

'''
lists are ideal for storing sets of numbers 
'''

# range() function makes it easy to generate a series of numbers
# range()'s one of the results is ex: range(1,5) , it can only print 1-4. this is the off-by one behavior


for value in range(1,5):
    print(value)

print()

for v in range(len(arr)):
    print(v)

print()

# using range() to make a list

numbers = list(range(1,6))
print(numbers)

# pass a third argument to range() , python uses that value as a step size when generating numberss

odd_numbers = list(range(1,16, 2))
print(odd_numbers)

squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
print(squares)
# squares = [i **2 for i in range(1, 11)]  == codes above

print()

print(min(squares))
print(max(squares))
print(sum(squares))

'''
working with part of a list
'''

# slicing a list

plays = ['charles', 'marthina', 'michael', 'florence', 'eli']
print(plays[0:3])
# python stops one item before the second index you specify

print(plays[:3])
print(plays[2:])
print(plays[-2:])


'''
Tuples
list : work well for sorting collections of items. they can change throughout the life of a program.  use  []
tuples:  it is immutable list, you can not change anything. use ()

'''
print()
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#you can assign a new value to a tuple
dimensions = (600,300)
for d in dimensions:
    print(d)