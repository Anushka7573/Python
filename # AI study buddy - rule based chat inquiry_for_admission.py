# AI study buddy - rule based chat assistant
# Rule based ai python chatbot

import datetime
import time

name = input("Swagat hai, enter your name: ")
presenthour = datetime.datetime.now().hour

if 5 <= presenthour <= 11:
    print("Good Morning,", name)
elif 11 <= presenthour <= 17:
    print("Good Afternoon,", name)
elif 17 <= presenthour <= 20:
    print("Good Evening,", name)
else:
    print("Good Night,", name)

print("Namaste! Welcome to Admission Inquiry Chatbot")
print("You can ask admission related questions. Type 'bye' to exit.")

# chatbot memory creation [dictionary of responses]

responses = {

    # basic greeting
    "hello": "Hi, welcome. How can I help you with admission?",
    "how are you": "I am fine. Thank you!",
    "who are you": "I am an AI admission inquiry chatbot.",

    # 🎓 Basic Admission Questions
    "admission kab start": "Admissions usually start in June every year.",
    "last date": "The last date for admission is usually July end. Please check the official website.",
    "courses available": "We offer courses like BCA, BBA, BSc IT, and MCA.",
    "course duration": "Most undergraduate courses are 3 years and postgraduate courses are 2 years.",
    "admission process": "You need to fill the application form, submit documents, and pay the admission fees.",

    # 📄 Eligibility Questions
    "eligibility": "Eligibility depends on the course. For most UG courses, you must pass 12th standard.",
    "minimum percentage": "Usually minimum 50% marks in the previous qualification are required.",
    "entrance exam": "Some courses require an entrance exam while others are merit based.",

    # 💰 Fees Related Questions
    "fees": "Course fees vary between ₹30,000 to ₹80,000 per year depending on the course.",
    "installment": "Yes, fees can be paid in installments.",
    "scholarship": "Yes, scholarships are available for meritorious and financially weak students.",

    # 📍 College Information
    "college kaha": "The college is located in Surat, Gujarat.",
    "hostel": "Yes, hostel facility is available for boys and girls.",
    "placement": "Yes, the college provides campus placement support.",

    # 📝 Application Questions
    "admission form": "You can fill the admission form online from the college website.",
    "online apply": "Yes, online application is available.",
    "documents": "Required documents include 10th marksheet, 12th marksheet, ID proof, and passport photo.",

    # 📞 Contact / Support
    "contact number": "You can contact the admission office at +91-9876543210.",
    "college visit": "You can schedule a visit by contacting the admission office.",
    "problem": "If you face any problem, please contact the admission helpdesk."
}

# method / function to get response of chatbot

def getresponsebot(userquestion):
    userquestion = userquestion.lower()

    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]

    return "Sorry, I don't have that information yet."

# Take user input

while True:

    userinput = input("Please ask your question: ")
    reply = getresponsebot(userinput)
    print("Bot response:", reply)

    if "bye" in userinput.lower():
        print("Thank you for using Admission Chatbot. Goodbye!")
        break