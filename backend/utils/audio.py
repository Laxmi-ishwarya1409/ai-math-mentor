import speech_recognition as sr

def speech_to_text(audio_path):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        return text
    except Exception:
        return "Could not understand audio. Please type the question."
