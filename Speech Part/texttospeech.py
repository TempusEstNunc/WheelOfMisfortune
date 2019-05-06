import pyttsx3

engine = pyttsx3.init()
engine.setProperty('volume',1.0)
engine.setProperty('rate',120)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.say('I demand a response.')
engine.runAndWait()


''' Note well: strings for voices that are needed
David (Male): HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
Zira (Female): HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0 '''
