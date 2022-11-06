list=["sofa","vacuum","blanket","chairs","cups","tables","cushions"]
for x in "list":
    print(list)
    print(list.insert(0,"bean bag"),"at the first position", list)
    print(list.insert(-1,"pencil"),"any position",list)
if "vacuum" in list:
   print("yes,'vacuum' is present")
if "pot" not  in list:
    print("no,'pot'is not present")