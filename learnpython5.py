import string

myNum= list(range(0,100))
print(myNum)

print(list(string.ascii_letters))

while True:
    var1 = input("Please enter any character, so that i will check whether its an alphabet : ")
    var1 = 9

    for item in list(string.ascii_letters):
        if item == var1:
            print("Its an alphabet")

    if var1 not in list(string.ascii_letters):
        print("Its not an alphabet")
    else:
        print("Its an alphabet")

 print("The 'A' is represented by an ascii code : ", ord('A'))
 print("The ascii code '97' is the letter -> ", chr(97))
 myAplhabets = list(string)