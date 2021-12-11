"""
Aquaponics Flask App
Dylan Lawrence
Evan Hinchliffe
"""
from flask import Flask, render_template
import mysql.connector
import json

app = Flask(__name__)


@app.route('/')
def liveTemp():
    return render_template('index.html')


credentials = json.load(open("code/front_app/credentials.json", "r"))


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

    action = cursor 
    action_table = ""

    for row in cursor:
        action_table += "<tr>"
        for observation in row:
            action_table += "<td>" + str(observation) + "</td>"

    cursor.close()
    database.close()
    return render_template('history.html', action = action)


@app.route('/status')
def status():
    return render_template('status.html')


if __name__ == '__main__':
    app.run(debug=True)
