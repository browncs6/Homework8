from flask import Flask, render_template, request
from glob import glob
from random import choice

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


# route for http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template('home.html')


# route for http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return render_template('about.html')


# route for http://127.0.0.1:5000/hello
# TODO: create /hello route and return "hello world" bolded as a full HTML5 document




# route for http://127.0.0.1:5000/greet
# route for http://127.0.0.1:5000/greet?user=<>&msg=<>
# TODO

if __name__ == '__main__':
    app.run(debug=True)
