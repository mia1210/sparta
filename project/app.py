<<<<<<< HEAD
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
    return jsonify({
        'result': 'success',
        'writer_list': writers, 
        'current_page': page,
        'total_count': total_count, 
        'total_page': total_page})

    return jsonify({'result': 'success','writer_list': writers, 'total_count': total_count, 'total_page': total_page})

@app.route('/api/list', methods=['POST'])
def writer_input():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    author_receive = request.form['author_give']
    title_receive = request.form['title_give']
    link_receive = request.form['link_give']
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    db.writer.update_one({'link':link_receive},{'$set':{'author':author_receive}})
    db.writer.update_one({'link':link_receive},{'$set':{'title':title_receive}})
    
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
=======
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
>>>>>>> 776cf777de749b3aeb83a90a4dd374247baa330a
