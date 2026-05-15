from fileinput import filename
import os

from flask import Flask,render_template,request



app= Flask(__name__)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html',person=name)


# @app.route('/login',methods=['GET','POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid

from flask import flash, redirect, url_for
from werkzeug.utils import secure_filename

# app.route('/upload',methods=['GET','POST'])
# def upload_file():
#     if request.method=='POST':
#         file=request.files['the_file']
#         file.save(f"var/uploads/{secure_filename(file.filename)}")


# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
   
# from flask import send_from_directory

# @app.route('/uploads/<name>')
# def download_file(name):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], name)

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # If the user does not select a file, the browser submits an
#         # empty file without a filename.
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''


from flask import make_response,abort,make_response,render_template

# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'),404


class User:

    def __init__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image=image

    def to_json(self):
        return {
            "username": self.username,
            "theme": self.theme,
            "image": self.image
        }


def get_all_users():

    users = [
        User("Apsar", "dark"),
        User("John", "light"),
        User("David", "blue")
    ]

    return users


@app.route("/users")
def users_api():

    users = get_all_users()

    return [user.to_json() for user in users]

        

def get_all_users():

    users = [
        User("Apsar", "dark", "profile.png"),
        User("John", "light", "john.png"),
        User("David", "blue", "david.png")
        
        ]

    return users
def get_current_user():

    user = User(
        username="Apsar",
        theme="dark",
        image="profile.png"
    )

    return user
@app.route("/me")
def me_api():

    user = get_current_user()

    return render_template(
        "me.html",
        username=user.username,
        theme=user.theme,
        image=user.image
    )

# @app.route("/")
# def home():
#     return render_template("me.html",username="Apsar",theme="",image="profile.png")
# from werkzeug.middleware.proxy_fix import ProxyFix
# app.wsgi_app = ProxyFix(app.wsgi_app)

@app.errorhandler(404)
def page_not_found(error):
    resp=make_response(render_template('error.html', error_code=404, message="Page not found", custom_header="A value"), 404)
    resp.headers['X-Something']='A value'
    return resp


import psycopg2 as pg
from flask import Flask, render_template
from application.db_config import DB_CONFIG


app = Flask(__name__)

@app.route('/')
def index():
    conn = pg.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("select * from actor")
    # rows = cur.fetchall()
    rows=cur.fetchmany(5)
    # rows=cur.fetchone()
    cur.close()
    conn.close()
    return render_template('app.html', rows=rows)







    