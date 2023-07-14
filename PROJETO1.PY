import openai
openai.api_key = "sk-kvfRyCEX4wm2tWBFLtMkT3BlpkFJajNxtHk9uvCu1sKpa4tc"

result = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the distance between the earth and mars?"}]
)

print(result)