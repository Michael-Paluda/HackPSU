from HackPSU2019.wikipedia_text import *
from HackPSU2019.markov.markov import *
from HackPSU2019.markov.main import *

while True:
    print("Enter an article to be read:")
    article_name = input()
    article = article_text(article_name)
    train_markov(article)

    summary = summarizer()
    print(summary)
    speak(summary)