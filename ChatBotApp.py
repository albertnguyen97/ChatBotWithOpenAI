import openai

openai.api_key = "your api key will find in settings of your account at platform openai"

input_message = input("input your question here")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write an essay about parents"}])

print(completion.choices[0].message.content)