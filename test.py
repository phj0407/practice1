
from flask import Flask
test = Flask(__name__)

@test.route('/')
def index():
    return 'index page : main'

@test.route('/page1')
def page1():
    return 'this is page1'

if __name__ == '__main__':
    test.run(debug=True)
