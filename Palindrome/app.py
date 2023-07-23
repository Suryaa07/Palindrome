from flask import Flask, request, render_template

app = Flask(__name__)

def is_palindrome(word):
    return word == word[::-1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def check_palindrome():
    word = request.form['word']
    result = is_palindrome(word)
    return render_template('index.html', word=word, result=result)

if __name__ == '__main__':
    app.run(debug=True)
