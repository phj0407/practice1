from flask import Flask, request, jsonify


app = Flask(__name__)

diary_temp = [
    {'date' : '20230828, ', 'contents' : '내용', 'userId':'user1' },
    {'date' : '20230829, ', 'contents' : '내용', 'userId':'user1'}]

@app.route('/')
def main():
    return 'home_page'

@app.route('/test/<userId>')
def get_userpage(userId):
    return jsonfy({'user' : userId})

@app.route('/test/<userId>', methods=['POST'])
def create_diary():
    new_diary = request.json
    #new_diary['date'] = 날짜가져오기
    diary_temp.append(new_diary)
    return jsonify( { 'message' : 'diary created successfully', 'diary' : new_diary} ), 201

@app.route('/test/<userId>/<int:date>', methods = ['PUT'])
def update_diary(date):
    updated_diary = request.json
    for diary in diary_temp:
        if diary['date'] == date:
            diary.update(updated_diary)
            return jsonify({ 'message' : 'diary updated successfully', 'diary' : diary} )
        return jsonify({ 'message' : 'diary not found'} ), 404
    
if __name__ == '__main__':
    app.run(debug=True)
    
