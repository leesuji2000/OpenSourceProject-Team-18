# generate_explanation/main.py
import sys
import os
import openai
from dotenv import load_dotenv

from .find_similar_word import find_similar_words


#src 폴더의 경로를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_list import prefix



prefixes = prefix.prefixes

load_dotenv()
gpt_key = os.getenv('GPT_KEY')
client = openai.Client(api_key=gpt_key)


def generate_explanation(word, meaning):
    stopGenerating = False
    for prefix in prefixes:
        if word.startswith(prefix[0]):
            base_word = word[len(prefix[0]):]
            print("case1")
            messages = [
                {"role": "system", "content": f"""너는 지금부터 한국인 어린이 영어 선생님이야. '{word}'가 영어 접두사 '{prefix[0]}' ({prefix[1]})로 이루어졌다면 뜻과 '{base_word}'를 사용하여 단어를 외우는 법을 알려줘 아니면 "비슷한 철자 연상법"을 사용해줘. """},
                {"role": "assistant", "content" : """Output : commemorate(기념하다)는 com-(함께)와 memorize(기억하다)의 합성어야.
                                                            많은 사람들과 기억한다는 것은 곧 기념한다는 것을 떠올릴 수 있어!"""},
                {"role": "user", "content": f"'{word}({meaning})'는 어원법으로 어떻게 외우는게 좋을까요?"}
            ]
            stopGenerating = True
            break
    if not stopGenerating:
        similar_words = find_similar_words(word)
        if similar_words:
            print("case2")
            base_words = similar_words[:3]
            messages = [
                {"role": "system", "content": f"너는 지금부터 어린이 영어 선생님이야. 영단어 '{base_words}'를 참고하여 철자가 비슷한 쉬운 단어를 하나 고르고, 고른 단어로 '{word}({meaning})'를 연상하여 외울 수 있는 방법을 제시해 줘."},
                {"role": "assistant", "content" : """Output : "bait(미끼)를 외우기 위해 wait(기다리다)라는 단어를 생각해봐. 이는 물고기가 bait(미끼)를 물 때까지 wait한다는 것을 떠울릴 수 있어!"""},
                {"role": "user", "content": f"'{word}({meaning})'라는 단어를 기억하는 좋은 방법은 뭐야? 한국어로 답변해줘."}
            ]
            '''for message in messages:
                print(message["content"])
                break'''
        else:
            print("case3")
            messages = [
                {"role": "system", "content": """너는 지금부터 어린이 영어 선생님이야. 영어 단어를 기억하는 데 도움이 되는 방법을 추천해줘. 아래 단계별로 진행해줘 
                                                1."사전에 있는 비슷한 발음 단어연상법", "사전에 있는 비슷한 철자 연상법", "합성어를 나눠서 뜻 설명" 중 가장 좋은 방법을 1개를 선택해.
                                                2. 1번에서 선택한 방법을 활용하여 암기법을 설명해. 연상법일 경우 두 단어를 연상할 수 있는 이유를 설명해줘.
                                                """},
                {"role": "assistant", "content" : """Output : bait을 외우기 위해 "비슷한 철자를 활용한 단어연상" 방법을 사용해보자.bait(미끼)를 외우기 위해 wait(기다리다)라는 단어를 생각해봐. 이는 물고기가 bait(미끼)를 물 때까지 wait한다는 것을 떠울릴 수 있어!"""},
                {"role": "user", "content": f"'{word}({meaning})'라는 단어를 기억하는 좋은 방법은 뭐야? 한국어로 답변해줘."}
            ]
    completion = client.chat.completions.create( 
        model="gpt-4o",
        messages=messages,
    )
    return (completion.choices[0].message.content)

"""#test
word = input("Enter an English word: ")
meaning = input("Enter the meaning of the word: ")
explanation = generate_explanation(word, meaning)
print(explanation)"""