def make_pizza(size, *topings):
    print(f"Making a {size}-inch pizza with the following toppins:")
    for topping in topings:
        print(f"-{topping}")