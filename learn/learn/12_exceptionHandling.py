try:
  getFile=open("learn/textD.txt","w")
  getFile.write("My file for exception handling")
except IOError:
  print("Unable to open or write to the file")
else:
  print("The file was written successfully")
finally:
    getFile.close()
    print("File is now closed")

##############

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
    
##############

def safe_divide(numerator,denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print("Cannot divide by Zero")
        return "Error"
    finally:
        print("Processing Complete")
numerator=int(input("Please enter a numerator value"))
denominator=int(input("Please enter a denominator value"))
print(safe_divide(numerator, denominator))

##############

import math

def calculation(number):
    try:
        result=math.sqrt(number)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value")

number1=float(input("Please enter a number"))
calculation(number1)

##############

def complex_calculation(num):
    try:
        result = num / (num - 5)
        print (f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")
# Test  case
user_input = float(input("Enter a number: "))
complex_calculation(user_input)
