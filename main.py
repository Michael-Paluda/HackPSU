import pickle, random

def summarizer():
    stored = open('stored.txt', 'rb')

    chain = pickle.load(stored)

    for key in chain.keys():
        print("key: " + key + "\tval: " + str(chain[key]))

    numS = 1

    def nextWord(word):
        if word not in chain.keys():
            return 'the'
        else:
            return random.choice(chain[word])


    # numS = int(input("How many sentences? "))
    numS = 10
    string = random.choice(list(chain.keys()))
    response = string
    # print(string)
    # print(chain[string])
    lastWord = string.split()[len(string.split()) - 1]
    lastWord2 = string.split()[0]
    while numS > 0:
        # print("TEST: " + lastWord + " " + lastWord2)
        temp = nextWord(lastWord2 + " " + lastWord)
        # print("TEMP: " + temp)
        response += " " + temp

        string = temp
        lastWord2, lastWord = lastWord, temp
        if temp[:-1] in "?.!,":
            numS -= 1
            response += "\n"
        # numS -=1
        # print(response)
    return response
