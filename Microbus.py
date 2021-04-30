#Version 3
#Modified condition to check user input

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


condition = True

while condition:
    print("How many passengers in the microbus ?")
    passengers = input("Enter a number: ")

    print("How much is the fare per passenger ?")
    fare = input("Enter a number: ")

    if (isfloat(passengers) & isfloat(fare)):
        condition = False
    if not isfloat(passengers):
        print("Passengers number was not entered correctly")
    if not isfloat(fare):
        print("Fare amount was not entered correctly")

#the input() function returns string
#thus we need to convert the strings to numbers as we calculate the result
result = float(passengers) * float(fare)

print("Total fare =",result)