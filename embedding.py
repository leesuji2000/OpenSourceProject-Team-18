import fasttext
from scipy import spatial
from difflib import SequenceMatcher
import heapq

# FastText 모델 로드
ft_model = fasttext.load_model('cc.ko.300.bin')

# 사전 정의된 단어 리스트, 영단어와 한국어 의미를 쌍으로 포함
words_list = [
    ['affection', '애정'], 
    ['car', '자동차'], 
    ['sadness', '슬픔'], 
    ['sweet_potato', '고구마'], 
    ['boat', '보트'],
    ['motorcycle', '오토바이'],
    ['happiness', '행복'],
    ['pizza', '피자'],
    ['anger', '분노'],
    ['fear', '두려움'],
    ['kimbap', '김밥'],
    ['scary', '무서움'],
    ['animal', '동물']
]

# 사용자 입력 단어
input_word = ['affextion', '사랑']

# 문자열 유사도를 계산하는 함수
def string_similarity(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

# 철자 유사도로 상위 N개 단어 선택 함수
def top_n_similar_spelling(input_word, words_list, n=5):
    similarities = []
    for word_pair in words_list:
        similarity = string_similarity(input_word, word_pair[0])
        heapq.heappush(similarities, (similarity, word_pair))
        if len(similarities) > n:
            heapq.heappop(similarities)
    
    # 최종 결과 반환 (가장 유사한 순으로 정렬)
    return sorted(similarities, reverse=True, key=lambda x: x[0])

# 의미적 유사도 계산 및 가중치 적용하여 최종 결과 반환
def find_best_match(input_word, words_list, ft_model, spelling_weight=0.7, semantic_weight=0.3):
    top_spelling_matches = top_n_similar_spelling(input_word[0], words_list)
    
    best_score = -1
    best_match = None
    
    for spelling_similarity, word_pair in top_spelling_matches:
        semantic_similarity = 1 - spatial.distance.cosine(
            ft_model.get_word_vector(input_word[1]),
            ft_model.get_word_vector(word_pair[1])
        )
        
        # 가중치 적용된 최종 점수 계산
        final_score = spelling_similarity * spelling_weight + semantic_similarity * semantic_weight
        
        if final_score > best_score:
            best_score = final_score
            best_match = word_pair
            
    return best_match

# 함수 호출 및 결과 출력
best_match = find_best_match(input_word, words_list, ft_model, 0.7, 0.3)
print(best_match)
