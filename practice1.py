# write a program to read a text from a given file certificcate.txt
#  and find
#  whether it contains the word live.

file= open("certificate.txt","r")
dataofFile= file.read()

dataofFile= dataofFile.lower()

if"live" in dataofFile:
    print("Yes Live word is present in the file")
else:
    print("No")