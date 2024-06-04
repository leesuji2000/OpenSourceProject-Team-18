from flask import Flask, Blueprint, request, redirect, url_for, render_template, current_app, g
#from src.check_word_validation import validate_word
from pymongo import MongoClient
from flask_pymongo import PyMongo


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_explanation import generate_explanation

app = Flask(__name__)
chooseMeaning_bp = Blueprint('chooseMeaning', __name__)


@chooseMeaning_bp.route('/select_meaning', methods=['POST'])
def select_meaning():
    db = g.db
    selected_meaning = request.form.get('selected_meaning')
    word = request.form.get('word')
    
    if not word or not selected_meaning:
        return '''
            <script type="text/javascript">
                alert("공백은 허용하지 않습니다");
                window.location.href = "/";
            </script>
            ''', 400
    return redirect(url_for('feedback.feedback', word=word, meaning=selected_meaning))