from flask import Flask, g
from src.routes.main_routes import main_bp
from src.routes.feedback_routes import feedback_bp
from src.routes.chooseMeaning_routes import chooseMeaning_bp
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
mongo_connect = "mongodb+srv://qaz8457:WlS6yzJyO93b4JLP@boca.dm5skx7.mongodb.net/?retryWrites=true&w=majority&appName=boca"

app.config["MONGO_URI"] = mongo_connect

@app.before_request
def before_request():
    g.db = db

# MongoDB 설정
client = MongoClient(mongo_connect)
mongo = PyMongo(app)
db = client.boca

# 블루프린트 등록
app.register_blueprint(main_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(chooseMeaning_bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)