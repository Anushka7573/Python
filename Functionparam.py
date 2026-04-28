# Function Defination with parameters
def average(a,b):  #average(2,3) defalt
    averageValue= (a+b)/2
    print(averageValue)


# Function Calling with Arguments
average(5,10)
average(9,10)
average(3,7)
average(5,8)    # average()

# write a function show_age(name,age) that prints: "anushka prajapati is 20 year old."

def show_age(name="anjali prajapati" ,age=18):
    print(f"{name} is {age} years old")

show_age("anushka prajapati",20)   
show_age()
show_age("aryan prajapti",23)