READ THIS FILE BEFORE USING SPEECH PROGRAM
The following prerequisites must be installed (preferrably with PyPi):
SpeechRecognition (pip install SpeechRecognition)
pyAudio (pip install pyAudio)
pyttsx3 (pip install pyttsx3)
pocketsphinx (pip install pocketsphinx)

NOTES:
Pocketsphinx, main recognition library, has ~80% accuracy rate. Time must be taken for model to adjust to voices of end user.
Pyttsx3 works flawlessly.
SpeechRecognition is just a wrapper for pocketsphinx, allows for greatly eased use of the complex library.
pyAudio is for microphone input in pocketsphinx/SpeechRecognition.

