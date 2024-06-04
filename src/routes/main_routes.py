from flask import Blueprint, request, redirect, url_for, render_template
import sys
import os

#src 폴더의 경로를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import get_korean_meaning

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form.get('word')
        #validation_error = validate_word(word)
        #if validation_error:
        #    return validation_error

        meanings = get_korean_meaning.kor_meaning_list(word)
        if not meanings:
            return '''
            <script type="text/javascript">
                alert("해당 단어 뜻을 찾을 수 없습니다");
                window.location.href = "/";
            </script>
            ''', 400
        return redirect(url_for('main.choose_meaning', word=word, meanings=meanings))
    return render_template('index.html')



@main_bp.route('/choose_meaning', methods=['GET'])
def choose_meaning():
    word = request.args.get('word')
    meanings = request.args.getlist('meanings')
    return render_template('chooseMeaning.html', word=word, meanings=meanings)
