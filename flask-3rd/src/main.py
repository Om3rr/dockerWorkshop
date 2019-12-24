from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    cat = requests.get("https://api.thecatapi.com/v1/images/search?size=full").json()[0]
    return render_template('index.html', url=cat.get("url"))
if __name__ == '__main__':
    app.run(host="0.0.0.0")
