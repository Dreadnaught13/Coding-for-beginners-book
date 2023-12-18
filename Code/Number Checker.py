#variables
numberholder = 0 #This will make a variable with the value 0

#script
numberholder = input("Please Enter Your Number [Less then 3]!")
numberholder = int(numberholder)
if numberholder < 4:
    print("Thank you this number is less then 3 so it's valid!")
else:
    print("That number is not valid due to it being more than 3")
