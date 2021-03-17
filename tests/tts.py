import pyttsx3
engine = pyttsx3.init()

# Configuração de voz para português
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

engine.say("Olá, Bem vindo!")
engine.runAndWait()

