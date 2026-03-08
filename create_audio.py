from gtts import gTTS

gTTS("what is the capital of japan").save("audio1.wav")
gTTS("who discovered gravity").save("audio2.wav")

print("audio files created")