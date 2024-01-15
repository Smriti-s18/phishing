from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def is_safe_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # You can add more checks based on your specific requirements
        return True
    except requests.exceptions.RequestException:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_url', methods=['POST'])
def check_url():
    url = request.form['url']
    is_safe = is_safe_url(url)
    return jsonify({'is_safe': is_safe})

if __name__ == '__main__':
    app.run(debug=True)
