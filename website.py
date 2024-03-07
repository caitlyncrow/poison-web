from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Obstacles')
def obstacles():
    return render_template('obstacles.html')

@app.route('/Identification')
def identification():
    return render_template('identification.html')

@app.route('/Types')
def types():
    return render_template('types.html')

@app.route('/Weaknesses')
def weaknesses():
    return render_template('weaknesses.html')

@app.route('/Solutions')
def solutions():
    return render_template('solutions.html')


if __name__ == "__main__":
    app.run(debug=True)

#What To Do If Can't Push Changes Right Away:
#cd data-poison-website
#git pull
#git push