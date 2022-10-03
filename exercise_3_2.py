# https://www.py4e.com/html3/03-conditional
# Exercise 3.2 Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    fh = float(hours)
    fr = float(rate)
except:
   print("Error, please enter numeric input")
   quit()

if fh > 40:
    # Overtime
    ovtH = fh - 40
    ovtP = ovtH * (fr * 1.5)
    pay = (40 * fr) + ovtP
else:
    # Regular
    pay = fh * fr

print("Pay:", pay)