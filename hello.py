# from unittest.mock import call
# from gevent.pywsgi import WSGIServer

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<p>Hello World.!</p>"

# def create_app():
#     return app

# if __name__=="__main__":
    
    
    # app.run(port=8080,debug=True,use_reloader=False,use_debugger=False,passthrough_errors=True)
    # http_server=WSGIServer(('',3000),app)
    # http_server.serve_forever()


from flask import request,Flask

app=Flask(__name__)

from markupsafe import escape

# @app.route('/hello')

# def hello():
#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"


# @app.route('/')
# def index():
#     return 'Index Page'
# @app.route('/hello')
# def hello():
#     return 'Hello, World!'


# from markupsafe import escape

# @app.route('/user/<username>')
# def show_user_name(username):
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f'Subpath {escape(subpath)}'

# @app.route('/project/')
# def show_project():
#     return 'The Project Page'

# @app.route('/about')
# def about():
#     return 'The About Page'

# from flask import url_for

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/about')
# def about():
#     return 'The About Page'

# @app.route('/login')
# def login():
#     return 'The Login Page'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\"s profile'

# with app.test_request_context():
#    print(url_for('index'))
#    print(url_for('about'))
#    print(url_for('login'))
#    print(url_for('login',next="/"))
#    print(url_for('profile',username='John Doe'))


from flask import request

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         input_username=input('username')
#         input_password=input('password')
#         if input_username=='admin' and input_password=='password':
#             return "Login Successful"
#         else:
#             return "Invalid Credentials"
#     else:
#         return "Show The Login Form"


@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
    
def show_the_login_form():
    return "Show The Login Form"
def do_the_login():
    return "Perform The Login"