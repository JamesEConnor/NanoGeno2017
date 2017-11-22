from random import *

#read all the text files into lists, allowing us to pick a word at random
adverbs = open("adverbs.txt")
adverbLines = adverbs.readlines()

for x in range(0,6000,1):
    adverbLines[x] = adverbLines[x].strip()

    
verbs = open("verbs.txt")
verbLines = verbs.readlines()

for y in range (0,30000,1):
    verbLines[y] = verbLines[y].strip()

adjectives = open("adjectives.txt")
adjLines = adjectives.readlines()

for z in range (0,28000,1):
    adjLines[z] = adjLines[z].strip()
    
nouns = open("nouns.txt")
nounLines = nouns.readlines()

for a in range (0,90000,1):
    nounLines[a] = nounLines[a].strip()


#From the ending of the verb, find te tense
def getTense(SentenceVerb):
    if(sentenceVerb.endswith('ed')):
        tense = -1
    elif(sentenceVerb.endswith('ing')):
        tense = 1
    else:
        tense = 0
    return tense

#from the ending of the noun, determine if it is plural or singular
def getPlural(sentenceNoun):
    if(sentenceNoun.endswith("s") and sentenceNoun.endswith("ness") == False and sentenceNoun.endswith("\'s") == False and sentenceNoun.endswith("us") == False and sentenceNoun.endswith("is") == False):
        plural =1
    else:
        plural = 0
    return plural

#from the ending of the verb and the tense, determine the subject of the sentence
def getSubject(sentenceVerb, tense):
    if (sentenceVerb.endswith("s") and tense == 0):
        subjectNum = randint(0,2)
        if(subjectNum == 0):
            subject = "She"
        elif(subjectNum == 1):
            subject = "He"
        else:
            subject = "It"
            
    else:
        subjectNum = randint(0,3)
        if(subjectNum == 0):
            subject = "I"
        elif(subjectNum == 1):
            subject = "You"
        elif(subjectNum == 2):
            subject = "We"
        else:
            subject = "They"
    return subject

#Take the values we found from the get functions, and use them to build the sentence
def applyGrammar(sentence, tense):
    sentenceList = sentence.split(" ")
    if(tense == 0 or tense == -1):
        sentenceList.insert(2,"the")
    else:
        sentenceList.insert(0,"will be")
        sentenceList.insert(3, "the")
    return sentenceList
runAgain = "yes"
while(runAgain.lower() == "yes"):
    numSentences = int(input("How many sentences would you like to generate? "))

    for x in range (0, numSentences, 1):
        #Get a random word from each part of speech
        randAdvb = randint(0,5999)
        sentenceAdverb = adverbLines[randAdvb]
        randVerb = randint(0,30000)
        sentenceVerb = verbLines[randVerb]
        randAdj = randint(0,27000)
        sentenceAdj = adjLines[randAdj]
        randNoun = randint(0,90000)
        sentenceNoun = nounLines[randNoun]

        #Create the beginning of the sentence, using each part of speech
        sentence = sentenceAdverb + " " + sentenceVerb + " " + sentenceAdj + " " + sentenceNoun
        #Get the tense, number and subject of the sentence, and use those values to build the sentence
        tense = getTense(sentenceVerb)
        plural = getPlural(sentenceNoun)
        subject = getSubject(sentenceVerb, tense)
        sentenceList = applyGrammar(sentence, tense)

        
        #Join the list back together to print the sentence as a single string
        print(subject, " ".join(sentenceList) + ".")
    runAgain = str(input("Generate more? "))
    while (runAgain.lower() != "yes" and runAgain.lower() != "no"):
         runAgain = str(input("Generate more? "))

    


    
    
