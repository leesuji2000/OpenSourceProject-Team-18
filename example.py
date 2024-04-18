import openai
import os 
from dotenv import load_dotenv #코드를 받아서 빌드하는 방법 사용



load_dotenv()  # take environment variables from .env.
gpt_key = os.getenv('GPT_KEY')
print(gpt_key)

openai.api_key = gpt_key
client = openai.Client(api_key=gpt_key)

PROFANITY_FILTER = ["fuck", "shit", "ㅅㅂ"]  # 욕설 입력 필터링

word = input("Enter an English word: ")
meaning = input("Enter the meaning of the word: ")

def generate_explanation(word, meaning):
    if word.lower() in PROFANITY_FILTER:
        return "Sorry, I can't assist with that."

    completion = client.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that uses mnemonic and other memory techniques to help users remember English words. Your responses should be in Korean."},
            {"role": "user", "content": f"What's a good way to remember the word '{word}'?"}
]
    )

    return completion.choices[0].message.content


explanation = generate_explanation(word, meaning)
print("----------------------result--------------------------")
print()
print(f"{explanation}")

print("------------------------------------------------------")