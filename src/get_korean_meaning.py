from bs4 import BeautifulSoup
import re
import requests
from check_word_validation.filtering import filter_message
from check_word_validation.moderation import checkModeration


#result code 0: success, 1: suggestion, 2: not found, 3: korean word, 4: filtering error, 5: empty word
def search_daum_dic(query_keyword):
    dic_url = "http://dic.daum.net/search.do?q={0}"
    r = requests.get(dic_url.format(query_keyword))
    soup = BeautifulSoup(r.text, "html.parser")
    if(query_keyword == ""):
        return [], 5
    elif not re.match(r'^[a-zA-Z\s]+$', query_keyword):
        return [], 3
    elif(filter_message(query_keyword) or checkModeration(query_keyword)):
        return [], 4
    # Check if the suggestion box with "혹시, 이것을 찾으세요?" is present
    suggestion_box = soup.find('strong', class_='tit_speller')
    if suggestion_box and "혹시, 이것을 찾으세요?" in suggestion_box.get_text():
        # Get the first suggested word
        first_suggestion = soup.find('a', class_='link_speller')
        if first_suggestion:
            first_suggested_word = first_suggestion.get_text()
            result_means = soup.find_all(attrs={'class': 'cleanword_type kuek_type'})
            definitions = get_meaning_list("daum", result_means)
            return definitions + [first_suggested_word], 1
    

    result_means = soup.find_all(attrs={'class': 'cleanword_type kuek_type'})
    if result_means:
        definitions = get_meaning_list("daum", result_means)
        return definitions, 0
    
    return [], 2

def get_meaning_list(site, result_means):
    results_list = []
    for elem in result_means:
        for item in elem.find_all("li"):  # Extract each list item containing the definition
            definition = item.get_text().strip()
            # Remove leading numbers and dots
            definition = re.sub(r'^\d+\.', '', definition).strip()
            if definition:
                results_list.append(definition)
    return results_list

def kor_meaning_list(query_keyword):
    try:
        result, status = search_daum_dic(query_keyword)
        return result, status
    except requests.ConnectionError:
        print("Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
