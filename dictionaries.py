'''
dictionary can store almost an limitless amount of data
a key-value pairs. each key is connected to a value . you can use key to access the value  associated with that key
a key's value can be a number, list, string, or another dictionary. any object you can crete
use { x : y }
when you present a key, python will return its value
you can add new key-value to a dictionary at any time because the dictionary is dynamic structure
'''

alien_o = {'color': 'green',
           'point': 5}

print(alien_o['color'])
print(alien_o['point'])

# adding new pairs

alien_o['x_position'] = 0
alien_o['y_position'] = 25

print(alien_o)

# modifying values in a dictionary => give the name of dictionary with the key and then the new value you want associated with

print()
alien_o['color'] = 'yellow'
print(f"the alien is now {alien_o['color']}")
print()

alien_y = {'x_position': 0,
           'y_position': 25,
           'speed': 'medium'}

print(alien_y['x_position'])
if alien_y['speed'] == 'slow':
    x_increment = 1
elif alien_y['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_y['x_position'] = alien_y['x_position'] + x_increment

print(f"new position: {alien_y['x_position']}")

# removing key-value pairs => you can use del with the name of key to remove the value

print()
del alien_y['speed']
print(alien_y)
print()

a = alien_o['color'].title()
print(a)

# using get() to access values.
# the get() method requires a key as a first argument. as a second optional argument, you can pass the value to be returned if the key doesn't exist

b = alien_o.get('place', 'not found')
print(b)

'''
looping through a dictionary
1: looping through all key-value pairs. 
    The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
2: looping through all the keys or values in a dictionary

'''
print()
user_o = {'username': 'abcdef',
          'first_name': 'justin',
          'las_name': 'dunno',
          'password': 12345, }

for key, value in user_o.items():
    print(f"\nKEY : {key}")
    print(f"\nVALUE: {value}")
print()

for name in user_o.keys():
    print(name.title())

print()

for value in user_o.values():
    print(value)
print()

key_names = ['username', 'password']

for name in user_o.keys():
    if name in key_names:
        v = user_o[name]
        print(f"\t{name.title()}, and its value is: {v}")

# key() isn't only for looping; it also returns  list of all keys
# you can return keys or values in a particular order by using sorted()
print()
n = {'a': 1,
     'b': 3,
     'f': 6,
     'e': 9,
     'c': 2,
     'g': 2,
     'g': 7}

for i in sorted(n.keys()):
    print(i)

for i in sorted(n.values()):
    print(i)
print()

# to see each element without repetition, we cna use a set(); a set is a collection in which each item  ust be unique
for s in set(n.values()):
    print(s)
print()
for k in set(n.keys()):
    print(k)
print()

# nesting => multiple dictionaries in a list, or a list of items aas a vlue in a dictionry
# you can nest dictionaries inside a list, a list of items inside a dictionary or even a dictionary inside another dictionary

d1 = {
    'color': 'green',
    'point': 5
}
d2 = {
    'speed': 'slow',
    'distance': 'NYC'
}
d3 = {
    'name': 'dunno',
    'age': 15
}

# it will become a list of dictionaries
d = [d1, d2, d3]
for i in d:
    print(i)

print()
# use range() to create a fleet of n aliens
f = []
for n in range(5):
    new_n = {'color': 'blue', 'speed': 5, 'brand': 'bmw'}
    f.append(new_n)

for c in f:
    print(c)
    print('---------------')
print()


print(f)
for n in f[:3]:
    if n['color'] == 'blue':
        n['color'] = 'black'
        n['speed'] = 1
        n['brand'] = 'toyota'

for n in f:
    print(n)

print()

# putting a list inside a  dictionary
# you can nest a list inside a dictionary any time you want more than one value to be associated with a single key
pizza ={
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(pizza)
print(pizza['crust'])
print(pizza.get('toppings'))
print()


'''
a dictionary in a dictionary
'''
users = {
    'host': {'name': 'justin', 'age': 33, 'location': 'phoenix'},
    'guest1': {'name': 'ashely', 'age': 30, 'location': 'LA'}
}

for n, a in users.items():
    print(f"\nUssername is: {n}, name is: {a['name']} , age is: {a['age']}, location is {a['location'].title()}")

