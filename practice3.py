# write a function that takes a string and returns the count of vowels and consonants separately.

def countVowConso(userInput):   # def fun(userInput):

    # define vowels
    vowels = "aeiouAEIOU"

    countVowel = 0
    countconsonants = 0

    # anushka123
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel= countVowel+1
            else:
                countconsonants+=1

    return countVowel,countconsonants 

# Function call 

vowels, consonants= countVowConso("anushka prajapati")
print(vowels,consonants)
print(vowels)