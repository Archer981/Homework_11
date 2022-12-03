from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index_page():
    items = [1, 2, 3]
    return render_template('index.html', items=items)


app.run()
