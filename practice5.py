# print how many lines are present in notes.txt

import os # renaming___

with open("notes.txt","r") as f:
    listofLines=f.readlines()
    print("output of readLines Function",listofLines)
    print("Number of Lines in File",len(listofLines))


# REMANING THE FILE 

# os.rename("report.txt","anushka.txt")
os.remove("anushka.txt")