import re

def filter_message(message):
    filtering_words = [
        'dick', 'fuck', 'shit', 'bastard', 'bitch', 'cum', 'cunt', 'sex',
        'damn', 'blowjob', 'ballsack', 'ass', 'arsehole', 'fag', 'faggot',
        'jizz', 'wank', 'prick', 'screw', 'twat', 'vagina', 'penis',
        'anal', 'orgasm', 'scrotum', 'nipple', 'masturbate', 'fucking',
        'cockhead', 'piss', 'pussylicking', 'rimming', 'suck', 'fucked'
    ]

    #독립된 경우에만
    bad_word_pattern = r'\b(' + '|'.join(filtering_words) + r')\b|(?<=\W)(' + '|'.join(filtering_words) + r')(?=\W)'
    match = re.search(bad_word_pattern, message.lower())
    if match:
        print(f'"{match.group()}" 단어 감지')
        return True
    else:
        return False