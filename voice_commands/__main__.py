from pathlib import Path

from .main import transcribe_audio

model_path = Path(__file__).parent / "models" / "vosk-model-small-ru-0.22"
transcribe_audio(str(model_path))
