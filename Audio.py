import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
from Commands import Commander

running = True

# def say(text):
    # subprocess.call('say' + text, shell=True)


def play_audio(file):
    chunk = 1024
    wf = wave.open(file, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()


def initSpeech():
    print("Listening...")
    # play_audio("./audio/ahem_x.wav")
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
    play_audio("./audio/Mouse.wav")
    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("couldn't understand you!")
    print("your command: ")
    print(command)
    if command == "quit":
        global running
        running = False
    cmd.discover(command)
   # engine.say("you said" + command)
    #engine.runAndWait()


while running:
    initSpeech()
