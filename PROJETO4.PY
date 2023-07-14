import openai
openai.api_key = "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"

audio_file = open("audio/german1.mp3", "rb")
result = openai.Audio.translate("whisper-1", audio_file)

print(result)