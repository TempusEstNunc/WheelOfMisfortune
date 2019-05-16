READ THIS FILE BEFORE USING SPEECH PROGRAM
The following prerequisites must be installed (preferrably with PyPi):
SpeechRecognition (pip install SpeechRecognition)
pyAudio (pip install pyAudio)
pyttsx3 (pip install pyttsx3)
pocketsphinx (special case: instructions on Linux below)

NOTES:
Pocketsphinx, main recognition library, has ~80% accuracy rate. Time must be taken for model to adjust to voices of end user.
Pyttsx3 works flawlessly.
SpeechRecognition is just a wrapper for pocketsphinx, allows for greatly eased use of the complex library.
pyAudio is for microphone input in pocketsphinx/SpeechRecognition.

Installing Pocketsphinx on Raspberry Pi:
Pi has trouble installing the program due to it being a cross-language program. It needs multiple dependencies to work.

Commands to run to install: 
1. sudo apt-get install -qq python python-dev python-pip build-essential swig git libpulse-dev libasound2-dev
2. git clone --recursive https://github.com/bambocher/pocketsphinx-python
3. cd pocketsphinx-python
4. python setup.py install

Additionally, pyttsx3 requires a dependency:
sudo apt-get install espeak
