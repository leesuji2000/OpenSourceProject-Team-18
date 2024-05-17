from flask import Flask, request, redirect, url_for, render_template
import re
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
import example 
import korMeaning



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
prohibited_words = ['sibal', 'ㅅㅂ', 'ㄱㅆㄲ', 'asshole', 'fuck']





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form.get('word')
        if any(prohibited_word in word for prohibited_word in prohibited_words):
            return '''
            <script type="text/javascript">
                alert("욕하지 마라");
                window.location.href = "/";
            </script>
            ''', 400
        if ' ' in word:
            return '''
            <script type="text/javascript">
                alert("공백은 허용하지 않는다");
                window.location.href = "/";
            </script>
            ''', 400
        if word:
            try:
                word.encode('ascii')
                if not word.isalpha():
                    raise ValueError
            except:
                return '''
                <script type="text/javascript">
                    alert("영어란엔 영어 똑바로 써라");
                    window.location.href = "/";
                </script>
                ''', 400
            words.append(word)
            print(words)
            meanings = korMeaning.kor_meaning_list(word)
            return redirect(url_for('choose_meaning', word=word, meanings=meanings))

            # Insert the data into the MongoDB
            #existing_word = db.bocas.find_one({"word": word})
            

            
            """if existing_word:
                return redirect(url_for('feedback', word=word, meaning=meaning, associative_memory=existing_word['associative_memory']))
            else: 
                db.boca.insert_one({"word": word, "meaning": meaning})
            return redirect(url_for('feedback', word=word, meaning=meaning)) 
        else:
            return '''
                <script type="text/javascript">
                    alert("공백은 허용하지 않는다");
                    window.location.href = "/";
                </script>
                ''', 400"""
    
    return render_template('index.html')

@app.route('/check100', methods=['GET'])
def check():
    # Query the MongoDB
    words = db.users.find()
    feedbacks = db.feedback.find()

    # Print the results
    # for word in words:
    #     print(word)
    # for feedback in feedbacks:
    #     print(feedback.get('feedback'))   
    # for feedback in feedbacks:
    #     print(feedback.get('score')) 
    count_100 = 0
    
    print('100점 받은 피드백') 
    print('-----------------')
    for feedback in feedbacks:
        
        if feedback.get('score') == '100':
            print(feedback)
            count_100 += 1
    print(count_100)
      

    return '콘솔에서 DB 확인하셈', 200

@app.route('/check50', methods=['GET'])
def check50():
    
    
    feedbacks = db.feedback.find()
    count_50 = 0
    
    print('50점 받은 피드백') 
    print('-----------------')
    for feedback in feedbacks:
        
        if feedback.get('score') == '50':
            print(feedback)
            count_50 += 1
    print(count_50)
      
    return '콘솔에서 DB 확인하셈', 200


@app.route('/check0', methods=['GET'])
def check0():
    
    feedbacks = db.feedback.find()
    count_0 = 0
    
    print('0점 받은 피드백') 
    print('-----------------')
    for feedback in feedbacks:
        
        if feedback.get('score') == '0':
            print(feedback)
            count_0 += 1
    print(count_0)
      
    return '콘솔에서 DB 확인하셈', 200



@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    data = None
    
    if request.method == 'GET':
        word = request.args.get('word')
        meaning = request.args.get('meaning')
        existing_word = db.bocas.find_one({"word": word})
        if existing_word:
            data = {
                'english_word': word,
                'meaning': meaning,
                'associative_memory': existing_word['associative_memory']
            }
        else:
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

@app.route('/chooseMeaning', methods=['GET', 'POST'])
def choose_meaning():
    if request.method == 'GET':
        word = request.args.get('word')
        meanings = request.args.getlist('meanings')  # 여러 의미를 리스트로 받음

        return render_template('chooseMeaning.html', word=word, meanings=meanings)
    
app.run(port=5000, debug=True)
