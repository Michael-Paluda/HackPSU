import wikipedia
import re
import win32com.client

def speak(string):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(string)


def article_text(article):
    try:
        page = wikipedia.page(article)
    except:
        speak('article not found, please be exact, did you mean')
        search_result=wikipedia.search(article)
        print(search_result)
        for possible in search_result:
            speak(possible)
        new_article = input("new article: ")
        article_text(new_article)


    content = page.content


    contentlist = content.split('== See also ==')

    content = ''.join(contentlist[0])

    content = re.sub('==','', content)
    content = re.sub('===','', content)
    content = re.sub('=','', content)
    '''
    indexes = []
    for i in range(len(content)):
        if content[i : i + 2] == '==':
            indexes.append([i, i+4 + content[i + 2:].find('==')])
    '''
    print(content)
    return content





