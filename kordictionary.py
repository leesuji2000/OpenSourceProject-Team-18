#참고한 github: https://gist.github.com/ultrakain/1ec00a17eebb1abfded81f91179aa9ff

import sys
import requests
from bs4 import BeautifulSoup
import re  # 정규 표현식 모듈 추가

def search_daum_dic(query_keyword):
    dic_url = "http://dic.daum.net/search.do?q={0}"
    r = requests.get(dic_url.format(query_keyword))
    soup = BeautifulSoup(r.text, "html.parser")
    # 결과를 담고 있는 요소의 구조를 정확히 지정해야 함
    result_means = soup.find_all(attrs={'class': 'cleanword_type kuek_type'})  # 클래스 이름은 예시이므로 정확히 확인 필요

    return print_result("daum", result_means)

def print_result(site, result_means):
    results_list = []
    for elem in result_means:
        for item in elem.find_all("li"):  # 정의가 담긴 각 리스트 항목을 추출
            definition = item.get_text().strip()
            # 숫자와 점을 제거
            definition = re.sub(r'^\d+\.', '', definition).strip()
            if definition:
                results_list.append(definition)
    return results_list

def main(args=None):
    """The main routine."""
    if len(sys.argv) < 2:
        query = input("Enter a keyword: ")
    else:
        query = sys.argv[1]
    
    try:
        result = search_daum_dic(query)
        print(result)
    except requests.ConnectionError:
        print("Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()