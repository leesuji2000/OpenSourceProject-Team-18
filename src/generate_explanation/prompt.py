def prefixPrompt(word, meaning):
    prefixPrompt  = [
{"role": "system", "content": f"""너는 지금부터 어린이 영어 암기법 서비스야. 반드시 단계별로 진행해. 자연스럽고 인간다운 방식으로 설명해. 마크다운 형식을 반드시 지켜줘. 어린이에게 부적절한 단어는 답변하지 말아줘."""},
{"role": "user", "content": f"입력 영단어 : / 입력 뜻 : 기념하다"},
{"role": "assistant", "content" : """
Output : 
## 1. 사용할 암기법: 어원을 활용한 암기법\n

## 2. 접두사 설명 및 예시:\n
- **접두사**: "com-"은 "함께" 또는 "함께, 같이"라는 의미를 갖고 있어.
- **관련 단어**:
    - **community** (공동체): 함께 모인 사람들.
    - **communicate** (소통하다): 함께 소통하다.
    - **compute** (계산하다): 여러 숫자들과 함께 계산하다.

## 3. 어근설명 및 예시:\n
- **어근**: "memor-"은 "기억"이라는 의미를 갖고 있어.
- **관련 단어**:
    - **memorize** (기억하다): 기억하다.
    - **memory** (기억): 기억.

## 4. 단어 해석:\n
commemorate는 다른 사람과 함께 기억하는 것은 곧 서로 기억한다고 생각할 수 있어. 그러면 이 뜻을 기억하기 쉽지 않을까?

## 5. 영어 예문:\n
Through this statue, we **commemorate** the memory of those who sacrificed their lives for our freedom.
(이 동상을 통해, 우리는 우리의 자유를 위해 목숨을 바친 사람들의 기억을 **기념하고** 있습니다.)"""},
{"role": "user", "content": f"입력 영단어 : '{word} / 외워야할 뜻 : {meaning}"}
]
    return prefixPrompt


def similarWordPrompt(word, meaning, similar_words):
    similarWordPrompt = [
{"role": "system", "content": f"""
 너는 어린이 영단어 연상 서비스야. 아래 단계별로 진행해줘.
 1. 비슷한 어린이 필수단어 중 {word}를 연상할 수 있는 단어와 뜻을 1개만 골라줘.
 2.  고른 단어로 '{word}({meaning})'를 연상하여 외울 수 있는 방법을 설명해. 인간적이고 자연스럽게 설명해.
 3. 영어 예문을 만들 때 설명한 내용을 사용하여 "비슷한 단어", "설명에 사용된 비슷한 단어"가 모두 들어간 하나의 쉬운 영어 예문을 작성하고 괄호로 한국어 뜻을 적어줘. 반드시 두 단어가 모두 들어가야 해.
 4.  들어간 두 단어는 볼딩처리 해줘. 예시의 Output 마크다운 형식을 반드시 지켜줘."""},
{"role": "user", "content": f"'입력 영단어 : bait / 입력 뜻 : 미끼' / 비슷한 어린이 단어 : [wait, weight]"},
{"role": "assistant", "content" : """
## 1. 사용할 암기법 : 비슷한 철자 연상법 \n
## 2. 'bait과 비슷한 철자 'wait'\n
**교과서 필수 영단어 : wait**\n
wait은 기다리다라는 뜻을 가지고 있어, bait(미끼)를 외우기 위해 미끼를 물 때 까지 기다린다고 생각해봐. 물고기가 bait(미끼)를 물 때까지 wait한다는 것을 떠울릴 수 있어!
## 3. 영어 예문\n
 
She **waited** for the **bait** to be taken by the fish.
(그녀는 물고기가 **미끼**를 물 떄 까지 **기다렸다.**)"""},
{"role": "user", "content": f"입력 영단어 : '{word} / 외워야할 뜻 : {meaning} / 비슷한 어린이 단어 : {similar_words}"}
]
    return similarWordPrompt

def generalPrompt(word, meaning):
    generalPrompt = [{"role": "system", "content": """
너는 지금부터 어린이 영어 암기법 서비스야. 영어 단어를 기억하는 데 도움이 되는 방법을 추천해줘. 아래 단계별로 진행해줘
1. 어린이에게 부적절한 단어는 답볂하지 말아줘.
2."비슷한 발음 영단어 연상암기법", "비슷한 철자 연상암기법", "합성어를 나눠서 뜻 설명 암기법" 방법 중 가장 좋은 방법을 1개만 선택해.
3. 선택한 방법을 활용하여 암기법을 설명해. 연상법일 경우 두 단어를 연상할 수 있는 이유도 설명해줘.
4. 설명한 내용을 시용하여 "질문한 단어", "설명에 사용된 비슷한 단어"가 모두 들어간 하나의 쉬운 영어 예문과 괄호로 한국어 뜻을 적어줘 반드시 두 단어가 모두 들어가야 해. 들어간 단어는 볼딩처리 해줘. 자연스럽고 인간다운 방식으로 설명해. 마크다운 형식을 반드시 지켜줘. 
"""},
{"role": "user", "content": f"'입력 영단어 : bait의 입력 뜻 : 미끼'"},
{"role": "assistant", "content" : """
Output : 
## 1. 사용할 암기법 : 비슷한 철자를 활용한 단어 연상 암기법 \n
 
## 2. 'bait과 비슷한 철자 'wait' \n
wait은 기다리다라는 뜻을 가지고 있어, bait(미끼)를 외우기 위해 미끼를 물 때 까지 기다린다고 생각해봐. 물고기가 bait(미끼)를 물 때까지 wait한다는 것을 떠울릴 수 있어!
 
## 3. 영어 예문 \n
She **waited** for the **bait** to be taken by the fish.
(그녀는 물고기가 **미끼**를 물 떄 까지 **기다렸다.**)"""},
{"role": "user", "content": f"입력 영단어 : '{word} / 외워야할 뜻 : {meaning}"}
]
    return generalPrompt