from modules import calc
from modules import leap
from modules import student
from modules import fib
from modules import fac
from modules import prime

def print_line():
    print("==========================================================================================================================================")

print_line()
print("Simple Calculator Demonstration")
print("Enter your two numbers separated by space in the following line.")

a,b=input().split()

a=float(a)
b=float(b)

print("Addition : ", calc.add(a, b))
print("Subtraction : ",calc.sub(a, b))
print("Multiplication : ",calc.multiply(a, b))
print("Division : ", calc.divide(a, b))
print_line()
print("Leap Year Demonstration")
year=int(input("Enter your year : "))
print("Is your year leap?", leap.is_leap(year))
print_line()
print("Student Division Demonstration")
student.start_calculation()
print_line()
print("Fibonacci Demonstration")
number=int(input("Enter number for your series : "))
print(fib.fib_series(number))
print_line()
print("Factorial Demonstration")
number=int(input("Enter your number : "))
print("Factorial is : ", fac.fac(number))
print_line()
print("Prime Number Demonstration")
number=int(input("Enter your number : "))
print("Is your number prime? ", prime.isPrime(number))
print("End Of Program. Thank You.")
print_line()
