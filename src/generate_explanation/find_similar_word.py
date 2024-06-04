import sys
import os

#src 폴더의 경로를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_list import goodWord
words = goodWord.goodword

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

def find_similar_words(user_word):
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

 