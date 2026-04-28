# create class student that takes 3 marks and has a method average().

class student:
    def __init__(self,name,listofmarks):
        self.name=name
        self.listofmarks=listofmarks

    def average(self):
        sum=0
        for eachvalue in self.listofmarks:
            sum=sum+eachvalue

        average=sum/3    
        print("average is :",average)

student1= student("anushka",[90,98,99])
student1.average()