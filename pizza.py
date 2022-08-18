def make_pizza(size, *toppings):
    print(f"\n making a {size} - inch pizza with thr following toppings: ")
    for topping in toppings:
        print(f"-{topping}")