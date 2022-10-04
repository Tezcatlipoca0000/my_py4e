# https://www.py4e.com/html3/04-functions
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# define the function
def computepay(hours, rate):
    if hours > 40:
        # Overtime
        ovtH = hours - 40
        ovtP = ovtH * (rate * 1.5)
        pay = (40 * rate) + ovtP
    else:
        # Regular
        pay = hours * rate
    return pay

# request user input
input_hours = input("Enter Hours: ")
input_rate = input("Enter Rate: ")

# convert input to float
try:
    fh = float(input_hours)
    fr = float(input_rate)
except:
   print("Error, please enter numeric input")
   quit()

# compute payment
total = computepay(fh, fr)

# print payment
print("Pay:", total)