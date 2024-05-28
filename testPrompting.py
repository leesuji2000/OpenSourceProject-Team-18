import openai
import os 
from dotenv import load_dotenv #코드를 받아서 빌드하는 방법 사용
from flask import Flask, request
from WordList import goodWord
import random

def one_char_diff(word1, word2):
    if word1 == word2:
        return False
    len1, len2 = len(word1), len(word2)
    if abs(len1 - len2) > 1:
        return False
    if len1 == len2:
        diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
        return diff_count == 1
    if len1 > len2:
        for i in range(len1):
            if word1[:i] + word1[i+1:] == word2:
                return True
    if len2 > len1:
        for i in range(len2):
            if word2[:i] + word2[i+1:] == word1:
                return True
    return False

def two_chars_diff(word1, word2):
    # 두 단어가 두 글자 차이나는지 확인합니다.
    if word1 == word2:
        return False
    len1, len2 = len(word1), len(word2)
    if abs(len1 - len2) > 2:
        return False
    if len1 == len2:
        diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
        return diff_count <= 2
    if len1 > len2:
        for i in range(len1):
            if one_char_diff(word1[:i] + word1[i+1:], word2):
                return True
    if len2 > len1:
        for i in range(len2):
            if one_char_diff(word2[:i] + word2[i+1:], word1):
                return True
    return False

def find_similar_words(user_word, words):
    similar_words = []
    diff_counts = []
    if len(user_word) <= 5:
        for word in words:
            if one_char_diff(user_word, word):
                similar_words.append((word, sum(1 for a, b in zip(user_word, word) if a != b)))
    else:
        for word in words:
            if two_chars_diff(user_word, word):
                similar_words.append((word, sum(1 for a, b in zip(user_word, word) if a != b)))
    # 철자 차이가 적은 순서대로 정렬합니다.
    similar_words.sort(key=lambda x: x[1])
    return [word for word, _ in similar_words]

words = goodWord.goodword

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
        ['over', '넘치는, 초과'],
        ['ambi', '양쪽, 양측'],
        ['auto', '자동'],
        ['bi', '두, 이중'],
        ['circum', '주위, 주변'],
        ['com', '함께, 공동'],
        ['con', '함께, 공동'],
        ['contra', '반대'],
        ['counter', '반대'],
        ['de', '없애다'],
        ['pre', '앞에'],
        ['pro', '앞에'],
        ['sub', '아래에'],
        ['super', '위에'],
        ['ab', '떨어져']

    ]
prefixes = sorted(prefixes, key=lambda x: len(x[0]), reverse=True) #길이가 긴 순서대로 정렬


app = Flask(__name__)
load_dotenv()  # take environment variables from .env.
gpt_key = os.getenv('GPT_KEY')
client = openai.Client(api_key=gpt_key)





# word = input("Enter an English word: ")
# meaning = input("Enter the meaning of the word: ")



def generate_explanation(word, meaning):
    stopGenerating = False
    for prefix in prefixes:
        if word.startswith(prefix[0]):
            base_word = word[len(prefix[0]):]
            print("case1")
            messages = [
                {"role": "system", "content": f"너는 지금부터 한국인 어린이 영어 선생님이야. 영어 접두사 '{prefix[0]}' ({prefix[1]})의 뜻과 '{base_word}'를 사용하여 단어를 외우는 법을 알려줘."},
                {"role": "assistant", "content" : """Output : commemorate(기념하다)는 com-(함께)와 memorize(기억하다)의 합성어야.
                                                            많은 사람들과 기억한다는 것은 곧 기념한다는 것을 떠올릴 수 있어!"""},
                {"role": "user", "content": f"'{word}({meaning})'는 어원법으로 어떻게 외우는게 좋을까요?"}
            ]
            stopGenerating = True
            break
    if not stopGenerating:
        similar_words = find_similar_words(word, words)
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

word = input("Enter an English word: ")
meaning = input("Enter the meaning of the word: ")
explanation = generate_explanation(word, meaning)

print(explanation)

