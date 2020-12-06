# pyttsx3 metinleri konusmaya donusturmeye yarar
import pyttsx3
# speech_recognition ses tanimaya yarar
import speech_recognition as sr
# os module isletim sisteminize komut vermeye yarar
import os


# take_commands() adinda bir fonksiyon yarattik
# bu fonksiyon sesinizi algilar, 
# herhangi bir hata yoksa soylediklerinizi taniyabilir ve geri donebilir
def take_commands():
    # konusma tanimayi baslatma
    r = sr.Recognizer()
    # bilgisayarin fiziksel mikrofonunun acilmasi
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # sesin ses degiskenine depolanmasi
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Google API kullanarak sesi tanima
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again")
            # hata varsa hicbirini dondurmez
            return "None"
    # sesi metin olarak dondurmek
    import time
    time.sleep(2)
    return Query


# Sesli asistanimiza konusma gucu vermek icin 
# Speak () fonksiyonu olusturduk
def Speak(audio):
    # pyttsx3 modulunu baslatma
    engine = pyttsx3.init()
    # engine.say() icine yazdigimiz her sey
    # sesli asistanimiz tarafindan soylenecek
    engine.say(audio)
    engine.runAndWait()

Speak("Do you want to shutdown your computer?")
while True:
    command = take_commands()
    if "no" in command:
        Speak("Okay I will not shut down the computer")
        break
    if "yes" in command:
        # Shutting down
        Speak("Shutting the computer")
        os.system("shutdown /s /t 30")
        break
    Speak("Say that again")