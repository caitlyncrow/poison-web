from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()

#What To Do If Can't Push Changes Right Away:
#cd data-poison-website
#git pull
#git push
    
def hello():
    return 0

def hello2():
    return 1