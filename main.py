# AI study buddy - rule based chat assitant
# Rule based ai python chatbot


import datetime
import time


name = input("swagat h,enter your name :")
presenthour= datetime.datetime.now().hour

if 5<=presenthour<=11:
    print("good morning,",name)
elif 11<=presenthour<=17:
    print("good afternoon,",name)
elif 17<=presenthour<=20:
    print("good evening,",name)
else:
    print("good night,",name)    


print("Namaste! welcome to your buddy chatbot ")
print("you can ask me basic question,type'bye' to exsit from the  bot ")

# chatbot memory creation [dictionary of responses]

responses={
    "hello": "hi, welcome.how can i help you?",
    "how are you": "i am very fine. thank you",
    "who are you": "i am smart ai chatbot",
    "motivate me": "keep going.every bug of your project makes you a beark",
    "happy": "great to hear that",
    "functions kya hota hai": "jakar chapter 7 padho"
}

# method / function to get response of chatbot

def getresponsebot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
        
    return " i am not able to tell that yet. mai jald hi ye sikh lunga"    
        

# Take user input

while  True:

    userinput=input("please ask your question:")
    reply=getresponsebot(userinput)      
    print("bot response:",reply)  

    if "bye" in userinput.lower():
        break