import pickle


def train_markov(article):
    text = article.split()

    chain = {}

    for i in range(len(text) - 3):
        try:
            if text[i + 2] not in chain[text[i] + " " + text[i + 1]]:
                chain[text[i] + " " + text[i + 1]] += [text[i + 2]]
        except:
            chain[text[i] + " " + text[i + 1]] = [text[i + 2]]
        if text[i] == "the":
            try:
                chain['the'] += [text[i + 1]]
            except:
                chain['the'] = [text[i + 1]]

    for key in chain.keys():
        print("key: " + key + "\tval: " + str(chain[key]))


    stored = open('stored.txt', 'wb')

    pickle.dump(chain, stored, 2)

    stored.close()