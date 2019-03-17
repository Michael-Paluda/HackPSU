import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


'''
while True:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)
'''


def speak(string):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(string)

