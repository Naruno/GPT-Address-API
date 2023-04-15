import openai

API_KEY = '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'
openai.api_key = API_KEY


response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[{"role": "user", "content": "Hi" }]
)["choices"][0]["message"]["content"]

print(response)