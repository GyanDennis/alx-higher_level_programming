# Import the add function from the add_0 module
from add_0 import add

# Define variables a and b
a = 1
b = 2

# Call the add function with a and b as arguments and store the result in a variable called sum
sum = add(a, b)

# Print the result using string formatting
print("{0} + {1} = {2}".format(a, b, sum))
