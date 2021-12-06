from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/livetemp')
def index():
    return render_template('index.html')

@app.route('/')
def liveTemp():
    return render_template('liveTemp.html')

if __name__ == '__main__':
    app.run(debug=True)
