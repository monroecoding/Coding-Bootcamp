"""
Coding Bootcamp at Monroe Township Library

Class 5 Coding Examples
"""


#define a function using the def keyword, a name, and parameters
def say_hello():
    print("Hello!")

#functions don't run unless they are called
say_hello()


#functions can be defined with parameters, which are placeholders for values that will be passed in when the function is called
def add_numbers(num1, num2):
    print(num1 + num2)

#we can call a function multiple times and pass in different arguments each time
add_numbers(3,4)
add_numbers(6,7)


#the return keyword allows your function to return a value which can be used or saved as a variable
#a function with no return statement will return None
#once the function reaches a return statement, it jumps out of the function block
def square(num):
    return num ** 2
    print("This will not print!")

#function is called and passed an argument, runs function and saves result to variable
num_squared = square(3)
print(num_squared)


#you can set a default argument that will be used if no other argument is passed
def greeting(name="friend"):
    print(f"Hello, {name}!")

greeting("Amy") #when given an argument, will override the default value
greeting() #calling the function without the argument is also fine, it will use the default


#example of a function for printing concert tickets, if row and seat numbers are provided they print on ticket
#if not provided we just issue a general admission ticket
def print_ticket(number, row=None, seat=None):
    print(f"Ticket number: {number}")

    if row == None or seat == None:
        print("General Admission")
    else:
        print(f"Row: {row}, Seat: {seat}")

print_ticket(34)
print_ticket(35, row="C", seat=8)




