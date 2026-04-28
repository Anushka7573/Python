# take 3 food and store in list, pribnt list and length

food1 = input("Enter food1:")
food2 = input("Enter food2:")
food3 = input("Enter food3:")

# method1 list form
foodlist =[food1,food2,food3]

print(foodlist)
print(len(foodlist))

# method2 list form
foodlist=[]
foodlist.append(food1)
foodlist.append(food2)
foodlist.append(food3)

print(foodlist)
print(len(foodlist))