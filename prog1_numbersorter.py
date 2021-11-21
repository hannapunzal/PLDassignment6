# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.
import time
def sorter(a, b, c, d):
    if a >= b and b >= c and c >= d:
        print(f"Sorted: {a}, {b}, {c}, {d}")
    elif a >= b and b >= d and d >= c:
        print(f"Sorted: {a}, {b}, {d}, {c}")
    elif a >= c and c >= b and b >= d:
        print(f"Sorted: {a}, {c}, {b}, {d}")
    elif a >= c and c >= d and d >= b:
        print(f"Sorted: {a}, {c}, {d}, {b}")
    elif a >= d and d >= b and b >= c:
        print(f"Sorted: {a}, {d}, {b}, {c}")
    elif a >= d and d >= c and c >= b:
        print(f"Sorted: {a}, {d}, {c}, {b}")
    elif b >= a and a >= c and c >= d:
        print(f"Sorted: {b}, {a}, {c}, {d}")
    elif b >= a and a >= d and d >= c:
        print(f"Sorted: {b}, {a}, {d}, {c}")
    elif b >= c and c >= a and a >= d:
        print(f"Sorted: {b}, {c}, {a}, {d}")
    elif b >= c and c >= d and d >= a:
        print(f"Sorted: {b}, {c}, {d}, {a}")
    elif b >= d and d >= a and a >= c:
        print(f"Sorted: {b}, {d}, {a}, {c}")
    elif b >= d and d >= c and c >= a:
        print(f"Sorted: {b}, {d}, {c}, {a}")
    elif c >= a and a >= b and b >= d:
        print(f"Sorted: {c}, {a}, {b}, {d}")
    elif c >= a and a >= d and d >= b:
        print(f"Sorted: {c}, {a}, {d}, {b}")
    elif c >= b and b >= a and a >= d:
        print(f"Sorted: {c}, {b}, {a}, {d}")
    elif c >= b and b >= d and d >= a:
        print(f"Sorted: {c}, {b}, {d}, {a}")
    elif c >= d and d >= a and a >= b:
        print(f"Sorted: {c}, {d}, {a}, {b}")
    elif c >= d and d >= b and b >= a:
        print(f"Sorted: {c}, {d}, {b}, {a}")
    elif d >= a and a >= b and b >= c:
        print(f"Sorted: {d}, {a}, {b}, {c}")
    elif d >= a and a >= c and c >= b:
        print(f"Sorted: {d}, {a}, {c}, {b}")
    elif d >= b and b >= a and a >= c:
        print(f"Sorted: {d}, {b}, {a}, {c}")
    elif d >= b and b >= c and c >= a:
        print(f"Sorted: {d}, {b}, {c}, {a}")
    elif d >= c and c >= a and a >= b:
        print(f"Sorted: {d}, {c}, {a}, {b}")
    else: 
        print(f"Sorted: {d}, {c}, {b}, {a}")

#ask four numbers
askName = input("Please enter your name: ")
time.sleep(1)
print(f"Hi, {askName}! Welcome to Number Sorter. Type the first number to proceed.")
print("...")
time.sleep(2)
firstNum = float(input("Enter first number: "))
secondNum = float(input("Enter second number: "))
thirdNum = float(input("Enter third number: "))
fourthNum = float(input("Enter fourth number: "))

#print four numbers from highest to lowest
sorter(firstNum, secondNum, thirdNum, fourthNum)
time.sleep(2)
print(f"Thank you for using this program. Hope to see you again next time, {askName}! ♥")
#combinations:
# 1234, 1243, 1324, 1342, 1423, 1432 
# 2134, 2143, 2314, 2341, 2413, 2431
# 3124, 3142, 3214, 3241, 3412, 3421 
# 4123, 4132, 4213, 4231, 4312, 4321