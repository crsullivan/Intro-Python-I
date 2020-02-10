# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):  
    if n % 2 == 0:
        print('true')
    else: 
        print('false')

is_even(2)
is_even(7)
is_even(26794)
is_even(45677689)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def check_num(num):  
    if num % 2 == 0:
        print('Even!')
    else: 
        print('Odd')

check_num(num)