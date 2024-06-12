from flask import Blueprint, request, redirect, url_for, render_template
import sys
import os

#src 폴더의 경로를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import get_korean_meaning

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form.get('word')
        #validation_error = validate_word(word)
        #if validation_error:
        #    return validation_error

        #result code 0: success, 1: suggestion, 2: not found, 3: korean word, 4: filtering error, 5: empty word
        meanings, resultCode = get_korean_meaning.kor_meaning_list(word)
        print("result",resultCode)

        if(resultCode == 0):
            mainString = "암기법을 보고 싶은 단어의 뜻을 선택해주세요"
        elif(resultCode == 1):
            newWord = meanings.pop()
            mainString = f"{word}을(를) {newWord}으로 수정한 결과입니다. 뜻을 선택하시거나 철자를 확인해주세요"
            word = newWord
        elif(resultCode == 2):
            return '''
            <script type="text/javascript">
                alert("해당 단어 뜻을 찾을 수 없습니다");
                window.location.href = "/";
            </script>
            ''', 400
        elif(resultCode == 3):
            return '''
            <script type="text/javascript">
                alert("한글 단어는 입력할 수 없습니다");
                window.location.href = "/";
            </script>
            ''', 400
        elif(resultCode == 4):
            filterMessage = meanings.pop()
            return f'''
            <script type="text/javascript">
                alert("필터링에 걸린 단어입니다. {filterMessage}");
                window.location.href = "/";
            </script>
            ''', 400
        elif(resultCode == 5):
            return '''
            <script type="text/javascript">
                alert("공백은 입력할 수 없습니다.");
                window.location.href = "/";
            </script>
            ''', 400
        return redirect(url_for('main.choose_meaning', word=word, meanings=meanings, mainString = mainString))
    return render_template('index.html')
    



@main_bp.route('/choose_meaning', methods=['GET'])
def choose_meaning():
    word = request.args.get('word')
    meanings = request.args.getlist('meanings')
    mainString = request.args.get('mainString')
    return render_template('chooseMeaning.html', word=word, meanings=meanings, mainString = mainString)
