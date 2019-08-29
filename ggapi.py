import speech_recognition as sr
import os, sys

# # Open a file
# path = "./DATA/dong/chat/"
# dirs = os.listdir(path)

# # This would print all the files and directories
# for file in dirs:
#     print(file)

r = sr.Recognizer()

with open("result_dongfr_ask_where.txt", "a") as text_file:

    path = "./DATA/dongfr/ask_where/"
    dirs = os.listdir(path)
    for file_name in dirs:
        with sr.WavFile(path + file_name) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(text_voice.lower() + "\n")
                print(path + file_name + " " + text_voice)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except LookupError:
                print("Could not understand audio")

with open("result_dongfr_ask_who.txt", "a") as text_file:

    path = "./DATA/dongfr/ask_who/"
    dirs = os.listdir(path)
    for file_name in dirs:
        with sr.WavFile(path + file_name) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(text_voice.lower() + "\n")
                print(path + file_name + " " + text_voice)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except LookupError:
                print("Could not understand audio")

with open("result_dongfr_chat.txt", "a") as text_file:

    path = "./DATA/dongfr/chat/"
    dirs = os.listdir(path)
    for file_name in dirs:
        with sr.WavFile(path + file_name) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(text_voice.lower() + "\n")
                print(path + file_name + " " + text_voice)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except LookupError:
                print("Could not understand audio")

with open("result_dongfr_greeting.txt", "a") as text_file:

    path = "./DATA/dongfr/greeting/"
    dirs = os.listdir(path)
    for file_name in dirs:
        with sr.WavFile(path + file_name) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(text_voice.lower() + "\n")
                print(path + file_name + " " + text_voice)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except LookupError:
                print("Could not understand audio")

with open("result_dongfr_introduce.txt", "a") as text_file:

    path = "./DATA/dongfr/introduce/"
    dirs = os.listdir(path)
    for file_name in dirs:
        with sr.WavFile(path + file_name) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(text_voice.lower() + "\n")
                print(path + file_name + " " + text_voice)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except LookupError:
                print("Could not understand audio")

with open("result_dongfr_lead_way.txt", "a") as text_file:

    path = "./DATA/dongfr/lead_way/"
    dirs = os.listdir(path)
    for file_name in dirs:
        with sr.WavFile(path + file_name) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(text_voice.lower() + "\n")
                print(path + file_name + " " + text_voice)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except LookupError:
                print("Could not understand audio")
