import speech_to_text, text_to_speech

def main():
    tts_control = text_to_speech.connect_to_editor()
    speech_to_text.speech_to_text(tts_control)
    text_to_speech.disconnect_from_editor(tts_control)


if __name__ == "__main__":
    main()
