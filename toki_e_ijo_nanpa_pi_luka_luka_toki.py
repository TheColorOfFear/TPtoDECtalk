def syllables(listIn):
    vowels=['a','e','i','o','u']
    consonants=['j','k','l','m','n','p','s','t','w']
    leonListin = []
    for i in range(len(listIn)):
        currentWord = list(listIn[i])
        #print(currentWord)
        sylWord = []
        currentSyl = []
        #print(len(currentWord))
        for i in range(len(currentWord)):
            if (consonants.count(currentWord[i])>0) and not(currentWord[i]=='n'):
                if i > 0:
                    sylWord.append(currentSyl)
                    currentSyl = []
                currentSyl.append(currentWord[i])
            elif currentWord[i]=='n':
                #print(i)
                if len(currentWord) > i+1:
                    if vowels.count(currentWord[i+1]) > 0:
                        if i > 0:
                            sylWord.append(currentSyl)
                            currentSyl = []
                        currentSyl.append(currentWord[i])
                    else:
                        currentSyl.append(currentWord[i])
                else:
                    currentSyl.append(currentWord[i])
            else:
                currentSyl.append(currentWord[i])
        sylWord.append(currentSyl)
        leonListin.append(sylWord)
    return leonListin

def decTalk(listIn, comp):
    misc=[]
    letters=['a','e','i','o','u','j','k','l','m','n','p','s','t','w']
    if comp.lower() == 'y':
        misc=['/', '\\', '"', ',', '.', '!', '?', '+']
    elif comp.lower() == 'n+':
        misc=[]
    else:
        misc=[',', '!', '?', '.']
    lettersDT=['aa','eh','iy','ow','uw','yx','k ','ll','m ','n ','p ','s ','t ','w ']
    output = ''
    for i in range(len(listIn)):
        word = i
        output = output + '`'
        for i in range(len(listIn[word])):
            syl = i
            for i in range(len(listIn[word][syl])):
                if letters.count(listIn[word][syl][i]) > 0:
                    letter = lettersDT[letters.index(listIn[word][syl][i])]
                else:
                    if listIn[word][syl][i].isalpha():
                        letter = '_'
                    else:
                        if misc.count(listIn[word][syl][i]) > 0:
                            letter = listIn[word][syl][i]
                        else:
                            letter = ''
                output = output + letter
            if not syl + 1 == len(listIn[word]):
                output = output + '-'
        if not word + 1 == len(listIn):
            output = output + ' '
    return output

CONT = ''
while CONT != 'x':
    putIn = input('Input a phrase in toki pona:\n').lower()
    miscSymb = input('Include syntax markings? (y/n/n+) \n')
    listyList = putIn.split()
    #print(putIn)
    #print(listyList)
    syl = syllables(listyList)
    #print(syl)
    DEC = decTalk(syl, miscSymb)
    print('\n' + DEC)
    CONT = input('\nInput X to close\nEnter to input again\n').lower()