#Lets start with a simple project

print("How many passengers in the microbus ?")
passengers = input("Enter a number: ")

print("How much is the fare per passenger ?")
fare = input("Enter a number: ")

#the input() function returns string
#thus we need to convert the strings to numbers as we calculate the result
result = int(passengers) * int(fare)

print("Total fare =",result)