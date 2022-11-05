
var1=10
var2=[1,2,5,3,55,9, 8, 5, 6, 3, 2, 1]

# print(set(var2), "No dups")
myColours = ["blue","green","yellow","white","pink","neon","teal","orange","black","brown"]
# mytColours = tuple(myColours)
# print(var1,myColours,var2)
# print(len(var2))
# print()
# print(len(myColours))
print("My colorful list", myColours, "\n")
print("Printing from the 4th element till end", myColours[3:5])

print(myColours.pop(3), "After removing 4th element", myColours)
print(myColours.append("purple"), "After adding purple", myColours)
print(myColours.insert(4, "red"), "After adding red at 5th position", myColours)

myColours.sort(reverse=True)
print("This is a sorted lest => ", myColours)



# print(myTColours, "Afetr removing 5th element", myTColours)
# pos = 0
# for x in myColours:
#
#     if x == "brown":
#         print("The position of yellow in the list is : ", pos)
#     pos = pos + 1

