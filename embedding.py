import fasttext
from scipy import spatial
from difflib import SequenceMatcher

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

# 입력 영단어와 사전에 정의된 영단어 중 철자가 가장 유사한 단어를 찾는 함수
def find_most_similar_spelling(input_word, words_list):
    highest_similarity = -1
    most_similar_word = None
    
    # 리스트 내의 각 영단어와의 철자 유사도를 계산
    for word_pair in words_list:
        similarity = string_similarity(input_word, word_pair[0])
        
        # 가장 높은 유사도를 갖는 단어 업데이트
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_word = word_pair
    
    return most_similar_word

# 함수 호출 및 결과 출력
# most_similar_spelling_word = find_most_similar_spelling(input_word[0], words_list)
# print(most_similar_spelling_word)

# 입력 한국어 단어와 사전에 정의된 한국어 단어 중 의미적으로 가장 유사한 단어를 찾는 함수
def find_most_similar_semantic(input_word, words_list, ft_model):
    # 입력 한국어 단어의 벡터를 얻음
    input_vector = ft_model.get_word_vector(input_word[1])
    
    # 유사도 계산을 위한 초기 설정
    highest_similarity = -1
    most_similar_word = None
    
    # 리스트 내의 각 한국어 단어와의 유사도를 계산
    for word_pair in words_list:
        word_vector = ft_model.get_word_vector(word_pair[1])
        similarity = 1 - spatial.distance.cosine(input_vector, word_vector)
        
        # 가장 높은 유사도를 갖는 단어 업데이트
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_word = word_pair
            
    return most_similar_word

# 가장 적합한 단어를 종합적으로 찾는 함수
def find_best_match(input_word, words_list, ft_model):
    # 먼저 철자 유사도로 가장 가까운 단어를 찾기
    spelling_match = find_most_similar_spelling(input_word[0], words_list)
    
    # 철자가 가장 유사한 단어 기준으로 의미적 유사도도 확인 (강조는 덜하지만 고려)
    semantic_match = find_most_similar_semantic(input_word, words_list, ft_model)
    
    # 여기서는 단순히 철자 유사도가 더 높은 단어를 반환하되 의미적 유사도도 고려한 결과를 출력
    if semantic_match and spelling_match[0] == semantic_match[0]:
        return semantic_match  # 의미와 철자 모두 일치
    return spelling_match

# 함수 호출 및 결과 출력
best_match = find_best_match(input_word, words_list, ft_model)
print(best_match)