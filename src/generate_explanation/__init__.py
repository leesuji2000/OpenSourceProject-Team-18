# generate_explanation/main.py
import sys
import os
import openai
from dotenv import load_dotenv
from .prompt import *
from .find_similar_word import find_similar_words


#src 폴더의 경로를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_list import prefix
from check_word_validation import filtering



prefixes = prefix.prefixes

load_dotenv()
gpt_key = os.getenv('GPT_KEY')
client = openai.Client(api_key=gpt_key)


def generate_explanation(word, meaning):
    stopGenerating = False
    for prefix in prefixes:
        if word.startswith(prefix[0]):
            print("case1")
            messages = prefixPrompt(word, meaning)
            stopGenerating = True
            break
    if not stopGenerating:
        similar_words = find_similar_words(word)
        if similar_words:
            print("case2")
            base_words = similar_words[:3]
            messages = similarWordPrompt(word, meaning, base_words)
        else:
            print("case3")
            messages = generalPrompt(word, meaning)
    completion = client.chat.completions.create( 
        model="gpt-4o",
        messages=messages,
    )
    filtering_result = filtering.filter_message(completion.choices[0].message.content)
    if(filtering_result):
            messages.append({"role": "system","content":"아이들을 위해서 반드시 순한 단어만 사용해서 설명해야 해"})
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