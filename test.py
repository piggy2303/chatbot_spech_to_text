import speech_recognition as sr

r = sr.Recognizer()

with open("result_minhanh_greeting.txt", "a") as text_file:
    for i in range(1, 49):
        voice_file = "Ghi âm của tôi " + str(i) + ".wav"
        with sr.WavFile("./DATA/minhanh/greeting/" + voice_file) as source:
            audio = r.record(source)
            try:
                text_voice = r.recognize_google(audio, None, "vi-VN" "en-US")
                text_file.write(text_voice.lower() + "\n")
                print(voice_file + " " + text_voice)
            except LookupError:
                print("Could not understand audio")