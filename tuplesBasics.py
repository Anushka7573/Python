 # tuples Basics

mytuple = (78,90,75)
studenttuple = ("Khushi","Divya","Ishaan")
print(len(mytuple))

# studenttuple[1] = "Aanchal" tuples are immutable/not changeable
print(studenttuple[2])

# empty tuples interview 10,13,14
emptytuple = ()
singletuple = (1,)
print(type(emptytuple))
print(type(studenttuple))
print(studenttuple.index("Divya"))
print(studenttuple.count("Khushi"))