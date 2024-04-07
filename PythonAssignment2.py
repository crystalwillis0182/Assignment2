#Introduction 
#A Python program consists of instructions written in the Python programming language. #These instructions are used to automate tasks, solve problems, and develop software #applications. The program is executed by an interpreter, which reads and executes the #instructions line by line.
#The most challenging part was t find a way to create the variable to multiple in using a #percent and calculating when the time will go off
#Get the charge for the food from the user using the input() function.


# Get the charge for the food from the user
charge = float(input("Enter the charge for the food: "))

#Calculate the tip by multiplying the charge by 18%.

#Calculate the sales tax by multiplying the charge by 7%.

#Calculate the total amount by adding the charge, tip, and tax.

#Display the results using the print() function.


# Calculate the tip
tip = charge * 0.18

# Calculate the sales tax
tax = charge * 0.07

# Calculate the total amount
total = charge + tip + tax

# Display the results
print("Tip:", "${:.2f}".format(tip))
print("Tax:", "${:.2f}".format(tax))
print("Total:", "${:.2f}".format(total))


#Step Two 

#Get the current time from the user using the input() function.

#Get the number of hours to wait for the alarm from the user using the input() function.

#Calculate the time when the alarm will go off by adding the current time and the number of hours to wait, and then taking the remainder when divided by 24.

#Display the alarm time using the print() function



# Get the current time from the user
current_time = int(input("Enter the current time (in hours): "))

# Get the number of hours to wait for the alarm from the user
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + hours_to_wait) % 24

# Display the alarm time
print("The alarm will go off at:", alarm_time)






