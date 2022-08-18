'''
functions are designed to do one specific task
have to call the function
'''


def greeting1():
    print("hello world")


greeting1()


# you can pass information (parameters) to a function
# parameters' order matters
'''
def greeting2(name):
    print(f"hello, {name}")


name = input('what is ur name: ')
greeting2(name)
'''

# keyword arguments => is a name- value pair that you pass to a function
def greeting3(name, age):
    print(f"hello, my name is {name}, and i am {age} old")


greeting3(name='justin', age=33)

'''
return values
function can process some data aand then return a value or set of values
the return statement takes a value from inside a function and sends it back to the line that called the function
'''

print('\\\\\\\\\\\\\\\\\\\\\\\\')
def get_name(fname, lname):
    full = f"{fname} {lname}"
    return full.title()


print(get_name('jimi', 'hendrix'))


'''
a function can return any kinda value you need it to, including more complicated data structures like lists and dictionaries
'''
'''
you can modify a list in a function. any changes made to the list inside the function's body are permanent
or
you can send a copy of a list to a function 

def function_name(list_name[:])

you can pass an arbitrary number of arguments.  when you dont know how many arguments a function needs to accept, you can do (*arguments)

'''

def make_pizza(*toppings):
    print(toppings)

make_pizza('musshrooms', 'green peppers', 'extra cheese')

'''
you can store your functions in a separate file called a module, and then importing that module into your main program
can import specific function from a module.

from module_name import function_name
'''
