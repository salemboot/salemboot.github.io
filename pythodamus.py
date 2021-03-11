import random

#verb=["work","fight","walk","fly","look","listen","try","eat","drink"]
#noun=["time","she","he","it","town","store","car","gas","sleep","bath","toliet"]
adverb=["often","seldom","went","almost","actually","too","then","yet","here","down","up","outside","inside","far","near"]
#adjective=["angry","happy","sad","excited","nice","mean"]
preposition=["above","below","front","side","right","left","beside","bottom","behind","to","on","off","inside","next","in","on","at","from","like","after","before","until","about","by"]
punctuation=["?","!","."]




verb=[]
with open('verbs.txt','r') as f:
    reader=f.read().split('\n')
    for row in reader:
        if(row != ''):
            verb.append(row)

noun=[]
with open('nouns.txt','r') as f:
    reader=f.read().split('\n')
    for row in reader:
        if(row != ''):
            noun.append(row)

adjectives=[]
with open('verbs.txt','r') as f:
    reader=f.read().split('\n')
    for row in reader:
        if(row != ''):
            adjectives.append(row)

print("\n\n\n\n\n\n\n\n\n\n"+random.choice(noun))
for x in range(7):
    for x in range(6):
        print(random.choice(noun).capitalize() + " " + random.choice(adverb) + " " +  random.choice(verb) + " " + random.choice(preposition) + " " + random.choice(noun) + random.choice(punctuation))
    print("\n")
