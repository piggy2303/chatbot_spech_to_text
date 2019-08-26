import speech_recognition as sr
import pyaudio
import wave

# if __name__=="__main__":
r = sr.Recognizer()
print("mic: ", sr.Microphone().list_microphone_names())
mic = sr.Microphone()
link_file = "speech_data.txt"

with open(link_file, 'a', encoding='utf-8') as file_obj:
    with mic as source:
        while (1):

            r.adjust_for_ambient_noise(source, 1)
            print("ready to record, please speak >> ")
            # audio = r.listen(source)

            with sr.WavFile("audio.wav") as source:
                audio = r.record(source)

                try:
                    text = r.recognize_google(audio, None, "vi-VN" "en-US")
                    if text == 'stop' or text == 'bye' or text == 'tạm biệt':
                        break
                    print(text)
                    file_obj.write(text + '\n')

                except sr.RequestError as e:
                    print(
                        "Uh oh! Couldn't request results from Google Speech Recognition service; {0}"
                        .format(e))

        file_obj.close()

        text = r.recognize_google(audio, None, "vi-VN" "en-US")
        print(text)
