#SpeechRecognition
#python3-pyaudio
#googletrans==3.1.0a0
#gtts
#playsound

import os
from random import choices
from re import M
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

translator = Translator()
microphone = sr.Recognizer()

def banner():
    print("""
 /$$$$$$  /$$           /$$                 /$$       /$$$$$$$$                                     /$$             /$$                        
 /$$__  $$| $$          | $$                | $$      |__  $$__/                                    | $$            | $$                        
| $$  \__/| $$  /$$$$$$ | $$$$$$$   /$$$$$$ | $$         | $$  /$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$ /$$__  $$| $$__  $$ |____  $$| $$         | $$ /$$__  $$|____  $$| $$__  $$ /$$_____/| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$|_  $$| $$| $$  \ $$| $$  \ $$  /$$$$$$$| $$         | $$| $$  \__/ /$$$$$$$| $$  \ $$|  $$$$$$ | $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/
| $$  \ $$| $$| $$  | $$| $$  | $$ /$$__  $$| $$         | $$| $$      /$$__  $$| $$  | $$ \____  $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$      
|  $$$$$$/| $$|  $$$$$$/| $$$$$$$/|  $$$$$$$| $$         | $$| $$     |  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
 \______/ |__/ \______/ |_______/  \_______/|__/         |__/|__/      \_______/|__/  |__/|_______/ |__/ \_______/   \___/   \______/ |__/      
                                                                                                                        By: Raphael Fiorin""")

def menu_translate_from():
    print("""

Transalate from:

1: Chinese (simplified)      6: Portuguese
2: Spanish                   7: Bengali
3: English                   8: Russian
4: Hindi                     9: Japanese
5: Arabic                    10: Punjabi/Lahnda
""")


def menu_translate_to():
    print("""

Transalate to:

1: Chinese (simplified)      6: Portuguese
2: Spanish                   7: Bengali
3: English                   8: Russian
4: Hindi                     9: Japanese
5: Arabic                    10: Punjabi/Lahnda
""")


def main():  # type: ignore
    banner()
    menu_translate_from()
    choise_from = input ("Choise: ")
    menu_translate_to()
    choise_to = input ("Choise: ")

# FROM CHINESE
    #Chinese to Chinese
    if choise_from == "1" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Chinese to Spanish
    if choise_from == "1" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Chinese to  English
    if choise_from == "1" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


    #Chinese to Hindi
    if choise_from == "1" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",dest='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


    #Chinese to Arabic
    if choise_from == "1" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


    #Chinese to Portuguese
    if choise_from == "1" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt-br')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


    #Chinese to Bengali
    if choise_from == "1" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


    #Chinese to Russian
    if choise_from == "1" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


    #Chinese to Japanese
    if choise_from == "1" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


    #Chinese to Punjabi/Lahnda
    if choise_from == "1" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='zh-cn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}")
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")

        return voice


# FROM SPANISH
    #Spanish to Chinese
    if choise_from == "2" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Spanish to Spanish
    if choise_from == "2" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Spanish to English
    if choise_from == "2" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Spanish to Hindi
    if choise_from == "2" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Spanish to Arabic
    if choise_from == "2" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Spanish to Portuguese
    if choise_from == "2" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Spanish to Bengali
    if choise_from == "2" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Spanish to Russian
    if choise_from == "2" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")
            

    #Spanish to Japanese
    if choise_from == "2" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")          


    #Spanish to Punjabi/Lahnda
    if choise_from == "2" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='es-es')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}")
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error") 


# FROM ENGLISH
    #English to Chinese
    if choise_from == "3" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Spanish
    if choise_from == "3" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to English
    if choise_from == "3" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Hindi
    if choise_from == "3" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Arabic
    if choise_from == "3" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Portuguese
    if choise_from == "3" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Bengali
    if choise_from == "3" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Russian
    if choise_from == "3" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Japanese
    if choise_from == "3" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #English to Punjabi/Lahnda
    if choise_from == "3" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='en')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}")
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


# FROM HINDI
    #Hindi to Chinese
    if choise_from == "4" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to Spanish
    if choise_from == "4" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to English
    if choise_from == "4" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to Hindi
    if choise_from == "4" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to Arabic
    if choise_from == "4" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to Portuguese
    if choise_from == "4" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to Bengali
    if choise_from == "4" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to Russian
    if choise_from == "4" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Hindi to Japanese
    if choise_from == "4" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")



    #Hindi to Punjabi/Lahnda
    if choise_from == "4" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='hi')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pa')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")



# FROM ARABIC
    #Arabic to Chinese
    if choise_from == "5" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Spanish
    if choise_from == "5" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to English
    if choise_from == "5" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Hindi
    if choise_from == "5" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Arabic
    if choise_from == "5" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Portuguese
    if choise_from == "5" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Bengali
    if choise_from == "5" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt-br')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Russian
    if choise_from == "5" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Japanese
    if choise_from == "5" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Arabic to Punjabi/Lahnda
    if choise_from == "5" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ar')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pa')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")



# FROM PORTUGUESE
    #Portuguese to Chinese
    if choise_from == "6" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Spanish
    if choise_from == "6" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to English
    if choise_from == "6" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Hindi
    if choise_from == "6" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Arabic
    if choise_from == "6" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Arabic
    if choise_from == "6" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Portuguese
    if choise_from == "6" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt-br')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Bengali
    if choise_from == "6" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Russian
    if choise_from == "6" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Japanese
    if choise_from == "6" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Portuguese to Punjabi/Lahnda
    if choise_from == "6" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pt')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pa')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")



# FROM BENGALI
    #Bengali to Chinese
    if choise_from == "7" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to Spanish
    if choise_from == "7" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to English
    if choise_from == "7" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to Hindi
    if choise_from == "7" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to Arabic
    if choise_from == "7" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")



    #Bengali to Portuguese
    if choise_from == "7" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt-br')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to Bengali
    if choise_from == "7" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to Russian
    if choise_from == "7" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to Japanese
    if choise_from == "7" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Bengali to Punjabi/Lahnda
    if choise_from == "7" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='bn')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pa')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")            



# FROM RUSSIAN
    #Russian to Chinese
    if choise_from == "8" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Spanish
    if choise_from == "8" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to English
    if choise_from == "8" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Hindi
    if choise_from == "8" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Arabic
    if choise_from == "8" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Portuguese
    if choise_from == "8" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt-br')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Bengali
    if choise_from == "8" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Russian
    if choise_from == "8" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Japanese
    if choise_from == "8" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Russian to Punjabi/Lahnda
    if choise_from == "8" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ru')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pa')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")



# FROM JAPANESE
    #Japanese to Chinese
    if choise_from == "9" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Spanish
    if choise_from == "9" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to English
    if choise_from == "9" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Hindi
    if choise_from == "9" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Arabic
    if choise_from == "9" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Portuguese
    if choise_from == "9" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt-br')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Bengali
    if choise_from == "9" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Russian
    if choise_from == "9" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Japanese
    if choise_from == "9" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Japanese to Punjabi/Lahnda
    if choise_from == "9" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='ja')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pa')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")



# FROM Punjabi/Lahnda
    #Punjabi/Lahnda to Chinese
    if choise_from == "10" and choise_to == "1":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='zh-cn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='zh-cn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Spanish
    if choise_from == "10" and choise_to == "2":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='es')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='es')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to English
    if choise_from == "10" and choise_to == "3":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='en')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='en')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Hindi
    if choise_from == "10" and choise_to == "4":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='hi')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='hi')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Arabic
    if choise_from == "10" and choise_to == "5":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ar')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ar')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Portuguese
    if choise_from == "10" and choise_to == "6":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pt')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pt-br')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Bengali
    if choise_from == "10" and choise_to == "7":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='bn')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='bn')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Russian
    if choise_from == "10" and choise_to == "8":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ru')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ru')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Japanese
    if choise_from == "10" and choise_to == "9":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='ja')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='ja')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")


    #Punjabi/Lahnda to Punjabi/Lahnda
    if choise_from == "10" and choise_to == "10":

        with sr.Microphone() as source:
            os.system('clear')
            banner()
            microphone.adjust_for_ambient_noise(source)
            print("\nSay something to translate:")
            audio = microphone.listen(source)

        try:
            voice = microphone.recognize_google(audio,language='pa')
            print("\nYou say: " + voice)
            translated = translator.translate(f'{voice}',dest='pa')
            print("\nText translation: " + translated.text)
            print("""\nWould you like to hear the pronunciation?:

1- Yes
2- No
    """)
            rsp = input("Choise: ")

            if rsp == "1":
                pronunciation = gTTS(f"{translated.text}",lang='pa')
                print(f"\nThis is the pronunciation of {translated.text}:")
                pronunciation.save('sample.mp3')
                playsound('sample.mp3')
            else:
                print("Ok")
                
        except:
            print("Error")
main()