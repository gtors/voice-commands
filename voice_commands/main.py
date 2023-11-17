import json

import pyaudio
from vosk import KaldiRecognizer, Model


def transcribe_audio(model_path):
    model = Model(model_path)
    print("Model loaded")
    rec = KaldiRecognizer(model, 16000)

    # Create an interface to PortAudio
    pa = pyaudio.PyAudio()

    # Open the stream
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=4000,
    )

    print("Listening...")

    while True:
        # Read from the stream
        data = stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print(res["text"])

    res = json.loads(rec.FinalResult())
    print(res["text"])

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio interface
    pa.terminate()
