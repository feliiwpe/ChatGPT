import openai
openai.api_key = "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"

resultado = openai.Image.create(
prompt = "create an intergalactic city in the middle of the amazon",
n = 1,
size = "1024x1024"
)

print(resultado)