#Version 3
#Modified condition to check user input

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

passengers_list = []
passengers_reminder = []
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

print("How much did each passenger pay ?")
for passenger in range(0,int(passengers)):
    pay_passenger = float(int(input("Enter a number: ")))
    passengers_list.append(pay_passenger)
    pay_reminder = pay_passenger - float(fare)
    passengers_reminder.append(pay_reminder)

print("The reminders",passengers_reminder)
#print(len(passengers_reminder))

print("Each paid",passengers_list)
#print(len(passengers_list))
#the input() function returns string
#thus we need to convert the strings to numbers as we calculate the result
result = float(passengers) * float(fare)

print("Total fare =",result)