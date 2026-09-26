from flask import Flask, redirect, url_for, request, render_template
import random
import string

def ShortCode():
    length = 10
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string

app = Flask(__name__)

dict = {'123': 'https://www.google.com'}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    url = data.get('url')
    for k,v in dict.items():
        if v == url:
            return {'short_code': k}
    short_code = ShortCode()
    while short_code in dict:
        short_code = ShortCode()
    dict[short_code] = url
    return {'short_code': short_code}

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