# Dictionary Basics

student = {
    " name":"Anushka",
    "city": "Banaras",
    "age" : 16,
    "rollnumber" : 12
}


print(type(student))
print(student[" name"])
print(student)
print(student["city"])
student["city"]="Hyderabad"
print(student)
student["favsubject"] = "Maths"
print(student)

print(student.keys())