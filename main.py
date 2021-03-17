from vosk import Model, KaldiRecognizer
import os
import pyaudio

# Apontando o algoritmo para ler o modelo treinado na pasta "model-br"
model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Criando um loop continuo para ficar ouvindo o microfone
while True:
    # Lendo audio do microfone
    data = stream.read(4000)

    # Convertendo audio em texto
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())