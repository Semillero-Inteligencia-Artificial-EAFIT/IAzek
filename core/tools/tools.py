def chat_answer(messages):
    completion = client.chat.completions.create(
      model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
      messages=messages,
      temperature=1.1,
      max_tokens=140 ,
    )
    return completion.choices[0].message.content
