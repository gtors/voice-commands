
Instructions:
```bash
poetry install
wget https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip
7z x vosk-model-small-ru-0.22.zip -ovoice_commands/models/
poetry run python -m voice_commands
```
