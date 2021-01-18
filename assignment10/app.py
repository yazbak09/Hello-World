from flask import Flask, url_for, redirect, render_template,request, session
import mysql.connector

app = Flask(__name__)

from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)



@app.route('/')
def cv_fu():
    return render_template('cv.html')


if __name__ == '__main__':
    app.run(debug=True)
