from flask import Flask, redirect, url_for
import random
import string

length = 10
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print(random_string)

app = Flask(__name__)

dict = {'123': 'https://www.google.com'}

@app.route('/')
def main():
    html = ''
    with open('templates/index.html', 'r') as f:
        html += f.read(1024)
    return html

@app.route('/<short_code>')
def go_to_url(short_code):
    for k,v in dict.items():
        if k == short_code:
            return redirect(v)
    return redirect(url_for('page_not_found'))

@app.route('/page-not-found')
def page_not_found():
    html = ''
    with open('templates/page_not_found.html', 'r') as f:
        html += f.read(1024)
    return html