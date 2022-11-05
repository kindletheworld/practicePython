
list_product=["iphone","laptop","comp","ipad","airpods","headphones","tv","dvd",
              "taperec"]
print(list_product.insert (8,"vcr"),"after the 5th element",list_product)
print(list_product.insert(3,"modem"),"after the 2nd element",list_product)
print(list_product.insert(5,"router"),"before 6th element",list_product)
print(list_product.insert(0,"pc"),"at the end",list_product)
print(list_product.insert(1,"soundsys"),"in the middle",list_product)
print(list_product.insert(0,"console"),"at the end",type(list_product))
print(list_product.insert(5,"mac"),"before the 4th element",list_product)
for x in list_product:
    print(x)
i=0
while i<len(list_product):
    print(list_product[i])
    i=i+1
while i<len(list_product):
    print(list_product)
    i=i+1

















