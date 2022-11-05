print("This is a simple calculator")
print()
var1 = input("Please enter the first number: ")
var2 = input("Please enter the second number : ")
sum1 = int(var1) + int(var2)

if int(var1) > int(var2):
    diff1 = int(var1) - int(var2)

else:
    diff1 = int(var2) - int(var1)
mul1 = int(var1) * int(var2)

if int(var1)> int(var2):
    div1 = int(var1) / int(var2)

else:
    div1= int(var2) / int(var1)

while True:
    var3 = input("Please select sum for addition, diff for difference,mul for multipliccation, div for division and quit to exit:")
    if var3 == "sum":
        print("The sum of given numbers is : ", sum1)
    elif var3 == "diff":
        print("The difference of the given numbers is : ", diff1)
    elif var3 == "mul":
        print("the product of the given numbers is>>>> ",mul1)
    elif var3 == "div":
        print("the quotient of the given numbers is:",div1)
    elif var3 == "quit":
        break
    else:
        print("You've selected a wrong option, please select sum or diff or multiplication or division")
