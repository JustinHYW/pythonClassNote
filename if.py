cars = ['bmw', 'toyota', 'subaru', 'audi', 'handa']
for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print("not found")

# python is case sensitive

# to check whether two conditions are both true simultaneously, use the keyword and to combine the two conditional tests
# to check either or both of the items is true or not, use keyword or
# to check if a value is in a list, use keyword in
# you can also use keyword not to check whether a value is not in a list
v = 'toyota'

print()

if v in cars:
    print("found")
else:
    print("not found")

# if - elif - else chain => to test more than two possible situations
print()
age = 12
if age < 4:
    print('too young')
elif age < 18:
    print('not old enough')
else:
    print('legal')

print()

a = []
if a:
    for i in a:
        print(i)
    else:
        print('no')

