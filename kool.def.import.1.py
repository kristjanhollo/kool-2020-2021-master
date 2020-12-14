"""
# import whole module
import pizza (import pizza as p)

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(24, "pineapple", "halapeno", "cheese")

p.make_pizza(16, "pepperoni")
p.make_pizza(24, "pineapple", "halapeno", "cheese")
"""

"""
# import certain module from module
from pizza import make_pizza
make_pizza(16, "pepperoni")
make_pizza(24, "pineapple", "halapeno", "cheese")
"""

"""
#import and rename
from pizza import make_pizza as mp

mp(16, "pepperoni")
mp(24, "cheese", ....)

"""

