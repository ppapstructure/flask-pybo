from flask import Blueprint,url_for
from werkzeug.utils import redirect

# __init__.py 의 register_blueprint()의 url_prefix가 더 우선된다.
bp = Blueprint('main', __name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

