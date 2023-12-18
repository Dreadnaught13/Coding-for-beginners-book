#varibales
a = "null" #This is a variable that containts the value 'null'
#script
a = input("Please give me a number and i will tell you if its odd or even!") #This allows the user to input the value of the variable a
a = int(a) #This makes the variable's type and integer
print("The number you gave me is ", "Even" if ( a % 2 == 0 ) else "Odd") #This will check if the varaible a when divided by 2 equals 0, if it does it prints "even", otherwise "odd"
