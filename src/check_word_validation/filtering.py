import re

def filter_message(message):
    lower_filtering_words = [
        'dick', 'shit', 'bastard', 'bitch', 'cum', 'cunt',
        'damn', 'blowjob', 'ballsack', 'ass', 'arsehole', 'fag', 'faggot',
        'jizz', 'wank', 'prick', 'screw', 'twat', 'vagina', 'penis',
        'anal', 'orgasm', 'scrotum', 'nipple', 'masturbate',
        'cockhead', 'piss', 'pussylicking', 'rimming', 'suck','yellow monkey'
    ]

    strong_filter_words = ['fuck', 'sex', 'penis' ]


    #독립된 경우에만
    bad_word_pattern = r'\b(' + '|'.join(lower_filtering_words) + r')\b|(?<=\W)(' + '|'.join(lower_filtering_words) + r')(?=\W)'

    match_lower = re.search(bad_word_pattern, message.lower())

    if match_lower:
        print(f'"{match_lower.group()}" 단어 감지')
        return True
    else:
        for strong_filter_word in strong_filter_words:
            if message.lower() in strong_filter_word:
                return True
        return False