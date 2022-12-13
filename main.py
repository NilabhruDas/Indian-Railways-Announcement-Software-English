import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    # 1 - Generate May I have your attenction please
    audio = AudioSegment.from_mp3("Railway Train Announcement English.mp3")
    start = 10
    finish = 3900
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_enghish.mp3", format="mp3")

    # 2 is train no and name

    # 3 is Generate to-city

    # 4 - Generate via-city

    # 5 - Generate is now ready for departure from
    audio = AudioSegment.from_mp3("Railway Train Announcement English.mp3")
    start = 11500
    finish = 13500
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_enghish.mp3", format="mp3")

    # 7 - platform number
    audio = AudioSegment.from_mp3("Railway Train Announcement English.mp3")
    start = 14000
    finish = 15000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_enghish.mp3", format="mp3")

    # 9 - we wish you all a very happy and comfortable journey
    audio = AudioSegment.from_mp3("Railway Train Announcement English.mp3")
    start = 15900
    finish = 22000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_enghish.mp3", format="mp3")


def generateAnnouncement(fielname):
    df = pd.read_excel(fielname)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate train no and name
        textToSpeech(item['train_no'] + " " +
                    item['train_name'], '2_enghish.mp3')

        # 3 - Generate to-city
        textToSpeech("to"+" "+item['to'], '3_enghish.mp3')

        # 4 - Generate via-city
        textToSpeech("via"+""+item['via'], '4_enghish.mp3')

        # 6 - from
        textToSpeech(item['from'], '6_enghish.mp3')

        # 8 - Generate platform number
        textToSpeech(item['platform'], '8_enghish.mp3')

        audios = [f"{i}_enghish.mp3" for i in range(1, 10)]
        announcement = mergeAudios(audios)
        announcement.export(
            f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_english.xlsx")
