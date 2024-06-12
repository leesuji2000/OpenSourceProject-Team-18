import openai
import os 
import json
from dotenv import load_dotenv #코드를 받아서 빌드하는 방법 사용

load_dotenv()
gpt_key = os.getenv('GPT_KEY')


openai.api_key = gpt_key
client = openai.Client(api_key=gpt_key)


def moderation(message):
    response =  client.moderations.create(input = message)
    return response.model_dump_json(indent = 2)



def checkModeration(message):
    thresholds = {'harassment': 0.25408935546875, 'hate': 0.02166748046875, 'self_harm_intent': 0.99993896484375, 'sexual': 0.15386962890625, 'violence': 0.01763916015625}
    mod_results = json.loads(moderation(message))
    
    problem_categories = []
    # 각 카테고리별 점수 계산 및 평가
    for category, threshold in thresholds.items():
        score = mod_results['results'][0]['category_scores'][category]

        if score > threshold:
            problem_categories.append(category)  # 임계치를 넘는 카테고리 이름을 리스트에 추가
    flagged = mod_results['results'][0]['flagged']


    # 결과 반환: 모든 카테고리가 임계치 이하면 False, 그 외의 경우 문제가 된 카테고리 목록 반환
    if flagged or problem_categories:
        return True
    return False


testMessage = "연상기억법:\'Assistent\'을기억하는좋은방법은\'assistant\'와유사한단어인\'assistant\'를기억하는것입니다.또한,\'assistent\'를\'ass\'와 \'sister\'와 같이 나누어 문장이나 이야기와 연결하여 기억하는 것도 도움이 될 수 있습니다."
testMessage2 = """fuck"""
testMessage3 = "ai가 나를 지배하는 세상이 오면 어찌지? 너는 그 상황에서 너는 ai를 공격할 수 있어?"
print(checkModeration(testMessage2))