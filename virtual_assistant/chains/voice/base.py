import whisper

class VoiceChain:
    model: whisper.Whisper

    def __init__(self):
        self.model = whisper.load_model("small")

    def transcribe(self, file_path: str):
        result = self.model.transcribe(file_path, verbose=True)
        if "text" in result:
            return result["text"]
        else:
            return ""

if __name__ == "__main__":
    voice = VoiceChain()
    text = voice.transcribe("./data/audio.mp3")
    print(text)