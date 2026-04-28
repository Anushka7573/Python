# you are given a list of programming languages:
# ["Python","Java","C++","Python","Java","C"]
# Convert it into a set amd print how many unique languages Divya knows.

programmingList = ["Python","Java","C++","Python","Java","C"]
print(type(programmingList))

# how to convert a list into set

programmingSet = set(programmingList)
print(type(programmingSet))
print(programmingList)
print("Divya knows these many langauges",len(programmingSet))