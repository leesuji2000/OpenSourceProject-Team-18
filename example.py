import openai
import os 
from dotenv import load_dotenv #코드를 받아서 빌드하는 방법 사용
from flask import Flask, request


app = Flask(__name__)
load_dotenv()  # take environment variables from .env.
gpt_key = os.getenv('GPT_KEY')


client = openai.Client(api_key=gpt_key)

PROFANITY_FILTER = ["fuck", "shit", "ㅅㅂ"]  # 욕설 입력 필터링


@app.route('/generate', methods=['POST'])
def generate():
    word = request.form.get('word')
    meaning = request.form.get('meaning')
    explanation = generate_explanation(word, meaning)
    return explanation


# word = input("Enter an English word: ")
# meaning = input("Enter the meaning of the word: ")



def generate_explanation(word, meaning):
    # if word.lower() in PROFANITY_FILTER:
    #     return "Sorry, I can't assist with that."
    prefixes = [
        ['dis', '반대 또는 부정'],
        ['un', '부정'],
        ['re', '다시, 반복'],
        ['pre', '미리, -전에'],
        ['mis', '잘못된, 부적절한'],
        ['sub', '아래, -부'],
        ['inter', '서로, 상호간'],
        ['semi', '반'],
        ['anti', '반대'],
        ['de', '아래로, 벗어나는 것'],
        ['trans', '-넘어서, 건너편'],
        ['super', '위, 초-'],
        ['under', '아래'],
        ['over', '넘치는, 초과']
    ]
    prefixes = sorted(prefixes, key=lambda x: len(x[0]), reverse=True) #길이가 긴 순서대로 정렬
    for prefix in prefixes:
        if word.startswith(prefix[0]):
            base_word = word[len(prefix[0]):]
            messages = [
                {"role": "system", "content": f"You are a helpful assistant that uses etymology using English '{prefix[0]}' ({prefix[1]}) and '{base_word}' to help users understand the origin of English words. Your responses should be in Korean."},
                {"role": "user", "content": f"What's the origin of the word '{word}({meaning})'?"},
            ]
            break
        else:
            messages = [
                {"role": "system", "content": "You are a helpful assistant that uses mnemonic and other memory techniques to help users remember English words. Your responses should be in Korean."},
                {"role": "user", "content": f"What's a good way to remember the word '{word}({meaning})'?"}
            ]
    completion = client.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=messages
    )

    return completion.choices[0].message.content