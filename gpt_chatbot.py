# gpt chatbot
from config import my_key
import openai

# setting the api key
openai.api_key = my_key

def chat_gpt_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role':'user', 'content': prompt}]
    )

    # filter the response content
    return response.choices[0].message.content.strip()



if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit', 'break', 'bye', 'stop']:
            break

        response = chat_gpt_bot(user_input) # calling chat_gpt_bot function
        print('ChatBot: ', response)

print('Script stoped')