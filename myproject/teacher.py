  from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def wirter_list() :
    SORT_RECENT = 0
    SORT_TITLE = 1
    SORT_AUTHOR = 2
    SORT_LIKE = 3

    sort_type = request.args.get('sort_type')
    writers = list(db.writer.find({},{'_id':False}))
    if sort_type == SORT_RECENT:

    elif sort_type == SORT_TITLE:

    elif sort_type == SORT_AUTHOR:

    elif sort_type == SORT_LIKE:
    for item in writers:
        item['like'] = item['RT'] + item['favorites']
    writers = sorted(writers, key=lambda k: k['like'], reverse=True) 
    
    return jsonify({'result': 'success','msg': '연결되었습니다'})

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
    
  
  
  SORT_RECENT = 0
    SORT_TITLE = 1
    SORT_AUTHOR = 2
    SORT_LIKE = 3

    sort_type = request.args.get('sort_type')
    writers = list(db.writer.find({},{'_id':False}))
    if sort_type == SORT_RECENT:

    elif sort_type == SORT_TITLE:

    elif sort_type == SORT_AUTHOR:

    elif sort_type == SORT_LIKE:
    for item in writers:
        item['like'] = item['RT'] + item['favorites']
    writers = sorted(writers, key=lambda k: k['like'], reverse=True) 
    
    return jsonify({'result': 'success','msg': '연결되었습니다'})