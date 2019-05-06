import speech_recognition as sr
import pyaudio

grammar = 'WheelOText.fsg'
recog = sr.Recognizer()
with sr.Microphone() as source:
    print 'Speak, my son. '
    audio = recog.listen(source)


try:
    resultnon = str(recog.recognize_sphinx(audio, show_all = False))
    print('No grammar: '+resultnon)
    resultyea = str(recog.recognize_sphinx(audio, show_all = False, grammar=grammar))
    print('Using grammar: ' +resultyea)
except sr.UnknownValueError:
    print "Did not understand audio. Try again."
except sr.RequestError as e:
    print ("Sphinx error: {0}.".format(e))
