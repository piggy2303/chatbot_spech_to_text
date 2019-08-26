import speech_recognition as sr

r = sr.Recognizer()

with open("text.txt", "a") as text_file:
    for i in range(57, 67):
        voice_file = "Ghi âm của tôi " + str(i) + ".wav"
        with sr.WavFile("./DATA/" + voice_file) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(voice_file + " " + str(text_voice) + "\n")
                print("Trans" + text_voice)
            except LookupError:
                print("Could not understand audio")