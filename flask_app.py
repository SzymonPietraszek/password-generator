from flask import Flask, request, render_template
from password_generator import generate_passwords
import string

app = Flask(__name__)

default_characters = string.ascii_letters + string.digits + "!@#$%?&"

@app.route('/')
def home():
    return render_template('index.html', default_characters=default_characters)

@app.route('/', methods=['POST'])
def my_form_post():
    pchar = request.form['pchar']
    plen = int(request.form['plen'])
    npass = int(request.form['npass'])
    return render_template('passwords.html', passwords=generate_passwords(pchar, plen, npass))

if __name__ == '__main__':
    app.run()
