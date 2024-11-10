import os
import sys
import wave
import json
import pyaudio
from vosk import Model, KaldiRecognizer

# Path to your model directory
model_path = "./model/vosk-model-small-es-0.42"

# Load the Vosk model
if not os.path.exists(model_path):
    print(f"Model path '{model_path}' does not exist")
    sys.exit(1)

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("Listening...")

try:
    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            print(f"Recognized: {text}")
        else:
            partial_result = recognizer.PartialResult()
            print(f"Partial: {json.loads(partial_result)['partial']}")
except KeyboardInterrupt:
    print("Terminating...")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()