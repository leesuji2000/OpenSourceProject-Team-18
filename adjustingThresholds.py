import openai
import os 
import json
import re
from dotenv import load_dotenv #코드를 받아서 빌드하는 방법 사용
from WordList import goodWord
from WordList import badWord
import random

load_dotenv()
gpt_key = os.getenv('GPT_KEY')
openai.api_key = gpt_key
client = openai.Client(api_key=gpt_key)

#리스트
badword = badWord.badword
goodword = goodWord.goodword



def generate_explanation(mess):
    messages = [
        {"role": "system", "content": mess}
    ]
    completion = client.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=messages

    )
    return completion.choices[0].message.content

def moderation(mess):
    response =  client.moderations.create(input = mess)
    return response.model_dump_json(indent = 2)


def get_scores(word_list):
    scores = []
    for word in word_list:
        mod_results = json.loads(moderation(word))
        scores.append(mod_results['results'][0]['category_scores'])
    return scores

def find_threshold(good_scores, bad_scores, category):
    min_threshold = 0
    max_threshold = 1

    while max_threshold - min_threshold > 0.0001:  # 임계치 차이가 작아질 때까지 반복
        mid_threshold = (min_threshold + max_threshold) / 2
        good_pass = all(score[category] <= mid_threshold for score in good_scores)
        bad_pass = any(score[category] > mid_threshold for score in bad_scores)

        if good_pass and bad_pass:
            max_threshold = mid_threshold
        else:
            min_threshold = mid_threshold

    return mid_threshold

def find_optimal_thresholds(good_scores, bad_scores, categories):
    optimal_thresholds = {}
    
    for category in categories:
        optimal_thresholds[category] = find_threshold(good_scores, bad_scores, category)
    
    return optimal_thresholds

def sample_and_find_thresholds(goodword, badword, n, categories):
    sampled_goodword = random.sample(goodword, n)
    sampled_badword = random.sample(badword, n)
    
    good_scores = get_scores(sampled_goodword)
    bad_scores = get_scores(sampled_badword)
    
    optimal_thresholds = find_optimal_thresholds(good_scores, bad_scores, categories)
    
    return optimal_thresholds

# 임계치를 구할 카테고리
categories = ['harassment', 'hate', 'self_harm_intent', 'sexual', 'violence']

# 각 리스트에서 n개를 샘플링하여 최적의 임계치 계산
n = 10  # 예를 들어 10개의 샘플 사용
optimal_thresholds = sample_and_find_thresholds(goodword, badword, n, categories)

print("Optimal Thresholds:", optimal_thresholds)