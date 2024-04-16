from flask import Flask, request, render_template
import re
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
import db

app = Flask(__name__)
mongo_connect = "mongodb+srv://qaz8457:WlS6yzJyO93b4JLP@boca.dm5skx7.mongodb.net/?retryWrites=true&w=majority&appName=boca"
#app.config["MONGO_URI"] = "mongodb+srv://qaz8457:WlS6yzJyO93b4JLP@boca.dm5skx7.mongodb.net/"
app.config["MONGO_URI"] = mongo_connect

# Create a connection to the MongoDB server

client = MongoClient(mongo_connect)
mongo = PyMongo(app)
# Select the database
db = client.boca
collection = db.boca

words = []
meanings = []



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
            db.users.insert_one({"_id": word, "name": meaning})
            return '성공'
        else:
            return 'Invalid data', 400
    return render_template('index.html')

@app.route('/check', methods=['GET'])
def check():
    # Query the MongoDB
    words = db.users.find()

    # Print the results
    for word in words:
        print(word)

    return 'Check console for output', 200

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Handle the feedback submission here
        pass
    return render_template('feedback.html')

app.run(port=5000)
