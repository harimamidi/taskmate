from gtts import gTTS
from playsound import playsound

audio="speech.mp3"
language="en"
sp=gTTS(text="Hari loves Kavya and Kavya loves hari",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("******audio is playing*******")