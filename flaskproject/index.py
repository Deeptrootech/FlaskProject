from flask import Flask, Blueprint
from markupsafe import escape

from flask import url_for

app = Flask(__name__)

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index_func():
    return 'This is Index page'

#
# @app.get('/login')
# def login_get():
#     return show_the_login_form()
#
#
# @app.post('/login')
# def login_post():
#     return do_the_login()
#
#
# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'
#
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login_get'))
#     print(url_for('login_get', next='/'))
#     print(url_for('profile', username='John Doe'))
#
# if __name__ == "__main__":
#     app.run(debug=True)
