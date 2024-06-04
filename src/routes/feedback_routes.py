from flask import Blueprint, request, render_template, current_app,g
import markdown
import sys
import os

#src 폴더의 경로를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_explanation import generate_explanation

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    db = g.db
    data = {}
    if request.method == 'GET':
        word = request.args.get('word')
        meaning = request.args.get('meaning')
        existing_word = db.bocas.find_one({"word": word, "meaning": meaning})
        if existing_word:
            data = {
                'english_word': word,
                'meaning': meaning,
                'associative_memory': existing_word.get('associative_memory', '')
            }
            
        else:
            data = {
                'english_word': word,
                'meaning': meaning,
                'associative_memory': generate_explanation(word, meaning)
            }
            
            db.bocas.insert_one({"word": word, "meaning": meaning, "associative_memory": data['associative_memory']})
            
        data['associative_memory'] = markdown.markdown(data['associative_memory'])
        
    if request.method == 'POST':
        score = request.form.get('score')
        feedback_text = request.form.get('feedback-text')
        db.feedback.insert_one({"score": score, "feedback": feedback_text})
    
    return render_template('feedback.html', data=data)
