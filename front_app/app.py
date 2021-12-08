"""
Aquaponics Flask App
Dylan Lawrence
Evan Hinchliffe
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import mysql.connector
import json

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def liveTemp():
    return render_template('index.html')


credentials = json.load(open("../back_process/credentials.json", "r"))


@app.route('/history')
def history():
    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()
    query = 'SELECT * FROM temperature_data;'

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    database.close()
    return render_template('history.html', database="aquaponics", data = data,)


@app.route('/status')
def status():
    return render_template('status.html')


if __name__ == '__main__':
    app.run(debug=True)
