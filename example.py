import openai
import os 
from dotenv import load_dotenv #코드를 받아서 빌드하는 방법 사용
from flask import Flask, request

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
    for prefix in prefixes:
        if word.startswith(prefix[0]):
            base_word = word[len(prefix[0]):]
            messages = [
                {"role": "system", "content": f"접두사 '{prefix[0]}' ({prefix[1]})의 의미와 '{base_word}'를 사용하여 어원을 이해하는 데 도움이 되는 유용한 어시스턴트입니다. 답변은 한국어로 제공되어야 합니다."},
                {"role": "user", "content": f"'{word}({meaning})'를 어떻게 외우는게 좋을까요? 한국어로 답변해주세요."}
            ]
            break
        else:
            messages = [
                {"role": "system", "content": "영어 단어를 기억하는 데 도움이 되는 기억법과 기타 기술을 사용하는 유용한 어시스턴트입니다. 답변은 한국어로 제공되어야 합니다."},
                {"role": "user", "content": f"'{word}({meaning})'라는 단어를 기억하는 좋은 방법은 무엇인가요? 한국어로 답변해주세요."}
            ]
    completion = client.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=messages
    )

    return completion.choices[0].message.content