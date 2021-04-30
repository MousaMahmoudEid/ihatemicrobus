#Version 2
#Added condition to check user input

condition = True

while condition:
    print("How many passengers in the microbus ?")
    passengers = input("Enter a number: ")

    print("How much is the fare per passenger ?")
    fare = input("Enter a number: ")
    try:
        int(passengers)
        print("Verified passenger input is a number")
        int(fare)
        print("Verified fare input is a number")
        condition = False
    except:
        print("User input is invalid")
        
#the input() function returns string
#thus we need to convert the strings to numbers as we calculate the result
result = int(passengers) * int(fare)

print("Total fare =",result)