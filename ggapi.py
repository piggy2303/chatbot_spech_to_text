import speech_recognition as sr
import os, sys
import csv


def ggapi(people, intent):
    r = sr.Recognizer()

    with open("result_" + people + "_" + intent + ".txt", "a") as text_file:

        path = "./DATA/" + people + "/" + intent + "/"
        print(path)
        dirs = os.listdir(path)
        for file_name in dirs:
            with sr.WavFile(path + file_name) as source:
                audio = r.record(source)
                try:
                    text_voice = r.recognize_google(audio, None, "vi-VN"
                                                    "en-US")
                    text_file.write(text_voice.lower() + "\n")
                    print(path + file_name + " " + text_voice)
                except sr.UnknownValueError:
                    print(
                        "Google Speech Recognition could not understand audio")
                except LookupError:
                    print("Could not understand audio")


def merger_file():
    with open('intent.csv', mode='a') as result_file:
        result_writer = csv.writer(result_file,
                                   delimiter=',',
                                   quotechar='"',
                                   quoting=csv.QUOTE_MINIMAL)

        path = './result/ngan/'
        dirs = os.listdir(path)

        for file_text_read in dirs:
            file_intent = file_text_read.split("_")[2].split(".")[0]
            print(file_intent)

            intent_col = file_intent

            if file_intent == "leadway":
                intent_col = "command_lead_way"

            if file_intent == "askwhat":
                intent_col = "ask_what"

            if file_intent == "askwho":
                intent_col = "ask_who"

            if file_intent == "askwhere":
                intent_col = "ask_where"

            print(path + file_text_read)
            text_voice_people = open(path + file_text_read, mode='r')
            for line in text_voice_people:
                result_writer.writerow([intent_col, line.lower().rstrip()])

