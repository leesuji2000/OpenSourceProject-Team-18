from flask import Flask, request, redirect, url_for, render_template
import re
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os
import sys
import example


# print the current working directory
print("Current working directory:", os.getcwd())
# print the PYTHONPATH
print("PYTHONPATH:", sys.path)

app = Flask(__name__)
mongo_connect = "mongodb+srv://qaz8457:WlS6yzJyO93b4JLP@boca.dm5skx7.mongodb.net/?retryWrites=true&w=majority&appName=boca"
app.config["MONGO_URI"] = mongo_connect

# Create a connection to the MongoDB server
client = MongoClient(mongo_connect)
mongo = PyMongo(app)
# Select the database
db = client.boca


words = []
meanings = []
scores = []
feedbacks = []




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form.get('word')
        meaning = request.form.get('meaning')
        if ' ' in word or ' ' in meaning:
            return '''
            <script type="text/javascript">
                alert("공백은 허용하지 않는다");
                window.location.href = "/";
            </script>
            ''', 400
        if word and meaning:
            try:
                word.encode('ascii')
                if not word.isalpha():
                    raise ValueError
            except:
                return '''
                <script type="text/javascript">
                    alert("영어란엔 영어로 써라");
                    window.location.href = "/";
                </script>
                ''', 400
            if not re.match("[가-힣]+", meaning):
                return '''
                <script type="text/javascript">
                    alert("뜻은 한국어로 써라");
                    window.location.href = "/";
                </script>
                ''', 400
            words.append(word)
            meanings.append(meaning)
            print(words)    
            print(meanings) 
             # Insert the data into the MongoDB
            existing_word = db.boca.find_one({"word": word})
            if existing_word:
                return redirect(url_for('feedback', word=word))  
            else: 
                db.boca.insert_one({"word": word, "meaning": meaning})
            return redirect(url_for('feedback', word=word, meaning=meaning)) 
        else:
            return '''
                <script type="text/javascript">
                    alert("공백은 허용하지 않는다");
                    window.location.href = "/";
                </script>
                ''', 400
    
    return render_template('index.html')

@app.route('/check', methods=['GET'])
def check():
    # Query the MongoDB
    words = db.users.find()
    feedbacks = db.feedback.find()

    # Print the results
    for word in words:
        print(word)
    for feedback in feedbacks:
        print(feedback)
    

    return '콘솔에서 DB 확인하셈', 200

import example
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    data = None
    
    if request.method == 'GET':
        word = request.args.get('word')
        meaning = request.args.get('meaning')
        data = {
            'english_word': word,
            'meaning': meaning,
            'associative_memory': example.generate_explanation(word, meaning)
        }
        db.bocas.insert_one({"word": word, "meaning": meaning, "associative_memory": data['associative_memory']})
    
    if request.method == 'POST':
        score = request.form.get('score')
        feedback = request.form.get('feedback-text')
        scores.append(score)
        feedbacks.append(feedback)
        print(scores)   
        print(feedbacks)         
        db.feedback.insert_one({ "score": score, "feedback": feedback})
    return render_template('feedback.html', data=data)

app.run(port=5000, debug=True)
