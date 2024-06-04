#참고한 github : https://gist.github.com/ultrakain/1ec00a17eebb1abfded81f91179aa9ff

from bs4 import BeautifulSoup
import re
import requests

def search_daum_dic(query_keyword):
    dic_url = "http://dic.daum.net/search.do?q={0}"
    r = requests.get(dic_url.format(query_keyword))
    soup = BeautifulSoup(r.text, "html.parser")
    result_means = soup.find_all(attrs={'class': 'cleanword_type kuek_type'})
    return get_meaning_list("daum", result_means)


def get_meaning_list(site, result_means):
    results_list = []
    for elem in result_means:
        for item in elem.find_all("li"):  # 정의가 담긴 각 리스트 항목을 추출
            definition = item.get_text().strip()
            # 숫자와 점을 제거
            definition = re.sub(r'^\d+\.', '', definition).strip()
            if definition:
                results_list.append(definition)
    return results_list


def kor_meaning_list(query_keyword):
    try:
        result = search_daum_dic(query_keyword)
        return result
    except requests.ConnectionError:
        print("Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")