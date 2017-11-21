from random import *
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


while True:
    randAdvb = randint(0,5999)
    sentenceAdverb = adverbLines[randAdvb]
    #print(sentenceAdverb)
    randVerb = randint(0,30000)
    sentenceVerb = verbLines[randVerb]
    randAdj = randint(0,27000)
    sentenceAdj = adjLines[randAdj]
    randNoun = randint(0,90000)
    sentenceNoun = nounLines[randNoun]

    sentence = sentenceAdverb + " " + sentenceVerb + " " + sentenceAdj + " " + sentenceNoun
    #print(sentence)
    if(sentenceVerb.endswith('ed')):
        tense = -1
    elif(sentenceVerb.endswith('ing')):
        tense = 1
    else:
        tense = 0


    if(sentenceNoun.endswith("s") and sentenceNoun.endswith("ness") == False and sentenceNoun.endswith("\'s") == False and sentenceNoun.endswith("us") == False and sentenceNoun.endswith("is") == False):
        plural =1
    else:
        plural = 0
        

    if (sentenceVerb.endswith("s") and tense == 0):
        subjectNum = randint(0,1)
        if(subjectNum == 0):
            subject = "She"
        else:
            subject = "He"
    else:
        subject = "I"
    sentenceList = sentence.split(" ")
    if(tense == 0 or tense == -1):
        sentenceList.insert(2,"the")
        #print(sentenceList[0])
        #print(sentenceList[2])
    else:
        sentenceList.insert(0,"will be")
        sentenceList.insert(3, "the")
    #sentece = " ".join(sentenceList)
    


    print(subject, " ".join(sentenceList) + ".")

    


    
    
