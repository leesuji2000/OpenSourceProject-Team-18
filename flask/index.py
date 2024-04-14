from flask import Flask, request, render_template
import re


app = Flask(__name__)

words = []
meanings = []



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form.get('word')
        meaning = request.form.get('meaning')
        if word and meaning:
            try:
                word.encode('ascii')
                if not word.isalpha():
                    raise ValueError
            except:
                return 'Word must be in English', 400
            if not re.match("[가-힣]+", meaning):
                return 'Meaning must be in Korean', 400
            words.append(word)
            meanings.append(meaning)
            print(words)    
            print(meanings) 
            return 'Data stored successfully'
        else:
            return 'Invalid data', 400
    return render_template('index.html')


app.run(port=5000)
