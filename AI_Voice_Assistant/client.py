from openai import OpenAI
 
# pip install openai 
# if u saved the key under a different env var name, you can do
client = OpenAI(
  api_key="<Your Key Here>",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named B2 skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)