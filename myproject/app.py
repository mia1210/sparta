from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import math 
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def writer_list() :
    page = request.args.get('page')
    sort = request.args.get('sort')
    PAGE_SIZE = 30 
    START_IDX = PAGE_SIZE * (int(page) - 1)
    total_count = len(list(db.writer.find({},{'_id':False})))
    total_page = math.ceil(total_count / PAGE_SIZE)
    writers = list(db.writer.find({},{'_id':False}).skip(START_IDX).limit(PAGE_SIZE))

    return jsonify({'result': 'success','writer_list': writers, 'total_count': total_count, 'total_page': total_page})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)