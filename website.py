
#Sources: 
#ChatGPT
#https://youtu.be/5L6h_MrNvsk?si=4uDbgWpGHCEpTEEG

#Issue: The base.css file is not being applied to the base.html file.

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/obstacles')
def obstacles():
    return render_template('obstacles.html')

@app.route('/identification')
def identification():
    return render_template('identification.html')

@app.route('/types')
def types():
    return render_template('types.html')

@app.route('/weaknesses')
def weaknesses():
    return render_template('weaknesses.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')


if __name__ == "__main__":
    app.run(debug=True)

#What To Do:
#cd poison-web
#git add .
#git commit -m ""
#git pull
#git push
