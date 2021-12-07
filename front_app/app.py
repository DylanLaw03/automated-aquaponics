"""
Aquaponics Flask App
Dylan Lawrence
Evan Hinchliffe
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def liveTemp():
    return render_template('index.html')


@app.route('/history')
def history():
    return render_template('history.html', database="Test")


@app.route('/status')
def status():
    return render_template('status.html')


if __name__ == '__main__':
    app.run(debug=True)
