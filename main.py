from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
#Sintese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Apontando o algoritmo para ler o modelo treinado na pasta "model-br"
model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Criando um loop continuo para ficar ouvindo o microfone
while True:
    # Lendo audio do microfone
    data = stream.read(2048)

    # Convertendo audio em texto
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)

            if text == 'que horas são' or text == 'me diga as horas':
                speak(core.SystemInfo.get_time())