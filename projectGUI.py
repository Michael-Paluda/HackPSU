# Description: This program creates a  graphical
# user interface that takes in the temperature in
# fahrenheit and the windspeed and displays the
# Windchill.

# Author: Michael Paluda

# imports the tkinter and tkinter.messagebox modules.
import tkinter
import tkinter.messagebox
import re
import wikipedia
import win32com.client
import pickle
import random
import threading



#
class SpeakerGUI:
    summary = ''
    entry = ''
    temp = ''
    def __init__(self):


        # Creates the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Speaker")

        # Creates 5 frames to group the widgets.
        self.titleframe = tkinter.Frame()
        self.tempframe = tkinter.Frame()
        self.buttonframe = tkinter.Frame()
        self.outputframe = tkinter.Frame()


        # Creates the label for the top frame.
        self.title_label = tkinter.Label(self.titleframe, text = "Welcome to SummarAIze, the summary text to speak app!",font = ('verdana', 12))
        # Packs the widgets for the top frame.
        self.title_label.pack(side = 'top')

        # Creates a label and a data entry widget for the temperature frame.
        self.temp_label = tkinter.Label(self.tempframe, text = 'What do you want to hear about?: ')
        self.temp_entry = tkinter.Entry(self.tempframe, width = 10)
        # Packs the widgets for the temperature frame.
        self.temp_label.pack(side = 'left')
        self.temp_entry.pack(side = 'left')


        entry = self.temp_entry.get()
        # Creates a button widget for the button frame.
        self.speakbutton = tkinter.Button(self.buttonframe, text = 'Speak', command = self.local)
        self.printbutton = tkinter.Button(self.buttonframe, text = 'Print', command = self.change_value)
        #  Packs the widgets for the button frame.
        self.speakbutton.pack(side = 'left')
        self.printbutton.pack(side = 'right')
        self.value = tkinter.StringVar()

        self.outputlabel = tkinter.Label(self.outputframe, textvariable = self.value)

        self.outputlabel.pack(side = 'left')



        # Packs all of the frames.
        self.titleframe.pack()
        self.tempframe.pack()

        self.buttonframe.pack()
        self.outputframe.pack()



        # Enters the tkinter main loop.
        tkinter.mainloop()



    # Callback function for the calc_button
    def local(self):
        # Gets the values entered by the user
        # from the two entry widgets.
        try:
            temp = SpeakerGUI.entry
            SpeakerGUI.entry = self.temp_entry.get()
            page = wikipedia.page(SpeakerGUI.entry)
            content = page.content

            contentlist = content.split('== See also ==')

            content = ''.join(contentlist[0])

            content = re.sub('==', '', content)
            content = re.sub('===', '', content)
            content = re.sub('=', '', content)

            self.train_markov(content)

            if SpeakerGUI.summary == '' or SpeakerGUI.temp != SpeakerGUI.entry:
                SpeakerGUI.summary = self.summarizer()

            self.speak(SpeakerGUI.summary)

        except:
            tkinter.messagebox.showinfo("Error", "I could not find a wikipedia article " + self.temp_entry.get())


    def train_markov(self, article):
        text = article.split()

        chain = {}

        for i in range(len(text) - 3):
            try:
                '''
                if text[i + 2] not in chain[text[i] + " " + text[i + 1]]:
                '''
                chain[text[i] + " " + text[i + 1]] += [text[i + 2]]
            except:
                chain[text[i] + " " + text[i + 1]] = [text[i + 2]]
            if text[i] == "the":
                try:
                    chain['the'] += [text[i + 1]]
                except:
                    chain['the'] = [text[i + 1]]

        stored = open('stored.txt', 'wb')

        pickle.dump(chain, stored, 2)

        stored.close()

    def summarizer(self):
        stored = open('stored.txt', 'rb')

        chain = pickle.load(stored)

        def nextWord(word):
            if word not in chain.keys():
                return 'the'
            else:
                return random.choice(chain[word])

        numS = 10
        # numS = int(input("How many sentences? "))

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

    def speak(self, string):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(string)

    def change_value(self):

        try:
            SpeakerGUI.temp = SpeakerGUI.entry
            SpeakerGUI.entry = self.temp_entry.get()
            page = wikipedia.page(SpeakerGUI.entry)
            content = page.content

            contentlist = content.split('== See also ==')

            content = ''.join(contentlist[0])

            content = re.sub('==', '', content)
            content = re.sub('===', '', content)
            content = re.sub('=', '', content)

            self.train_markov(content)

            if SpeakerGUI.summary == '' or SpeakerGUI.temp != SpeakerGUI.entry:
                SpeakerGUI.temp = SpeakerGUI.entry
                SpeakerGUI.summary = self.summarizer()

            self.value.set(SpeakerGUI.summary)

        except:
            tkinter.messagebox.showinfo("Error", "I could not find a wikipedia article " + self.temp_entry.get())


# Creates an instance of the WindchillCalculatorGui class.
mygui = SpeakerGUI()

