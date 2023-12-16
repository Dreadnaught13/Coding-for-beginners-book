#imports:
import random

#variables:
name = "null" #This defines the variable name with the string "null"
randomnumber = random.randint(1,20)
number = "null"
loopholder = 0

#script:
name = input("What is your name? ") #This will allow the user to define the value of the variable 'name'
print("Lets play a game; im going to think of a random number and you have to guess it, i will tell you if its higher or lower depending on your awnser.")
while loopholder < 1: #This is will loop until the value of the variable 'loopholder' becomes more then 1
    number = input("Please enter the number: ") 
    if int(number) > randomnumber: #This statment can check if for a variables value and then decide what to do from there on out
        print("The number was lower, try agian")
    elif int(number) < randomnumber: #This is a branched if statment, quite like the last one i used
        print("The number was higher, try agian")
    else: #This is an else statment (it is also branched in the if statment), anything other than the things said in the first two if statments will be met with this response
        print("You Won Good Job")
        loopholder += 2 #this will add 2 to the value of loopholder (this will push the loopholders vaule to 3 ending the loop
