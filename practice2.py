# create a class laptop with attributes: brand, RAM, price. create 2 object with different values.

class laptop:
    brand="default"
    RAM="default 8GB"
    price="default 1 lakh"

laptop1=laptop()
laptop1.brand="mackbook"
laptop1.RAM="16GB"
print("laptop1 brand-",laptop1.brand)

laptop2=laptop()
laptop2.brand="lenova"
print("laptop2 brand-",laptop2.brand)