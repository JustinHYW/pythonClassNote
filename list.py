'''
a list is a collection of items in a particular order
it can include letters , digits
use []
'''


bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

print(bicycles[0])

print(bicycles[1].title())

print(bicycles[-1])  # -1 means the last one

'''
you can change , add, remove elements
'''

# modifying
bicycles[0] = "ducati"

print(bicycles)

#appending => append() add an element to the end of the list

bicycles.append('suzuki')

print(bicycles)

#inserting => insert an element at a specific position

bicycles.insert(3, 'yamaha')

print(bicycles)

#removing  1 => remove an item according to its position in the list  or accoirding to its value

del bicycles[-1]

print(bicycles)

# removing 2 => use pop() method.  pop() removes the last item in a list , but it lets you work with that item after removing it
# you can pop aan item from any position by putting an index in the pop(0)
bicycles.pop()
print(bicycles)

# removing 3 => use remove() . you can use it when you dont know the position of the item.
# remove() deletes only the first occurrence of the value
bicycles.remove('ducati')
print(bicycles)
a = 'redline'
bicycles.remove(a)
print(bicycles)

'''
organizing the list
'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
# sort() => sorting a list permanently

cars.sort()
print(cars)

#sorting in reverse
cars.sort(reverse=True)
print(cars)

#sorted() => let you display yout list in a particular order but doesn't aaffect the actual order of the list
print(sorted(cars))

'''
printing a list in reverse order by using reverse(), permanently
'''
cars.reverse()
print(cars)

'''
finding the length of a list
'''
print(len(cars))

'''
always use index -1 when you want to access the last item in the list
'''