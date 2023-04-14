from faster_whisper import WhisperModel


class WhisperModelWrapper:
    def __init__(self):
        self.model_size = "small"
        self.model = WhisperModel(
            self.model_size, device="cpu", compute_type="int8"
        )

    def transcribe(self, audio):
        segments, _ = self.model.transcribe(
            audio=audio, beam_size=5, language="ja", word_timestamps=True
        )
        return segments
