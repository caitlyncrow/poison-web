
#Sources: 
#ChatGPT
#https://youtu.be/5L6h_MrNvsk?si=4uDbgWpGHCEpTEEG
#https://youtu.be/y62Dvo2Ml7o?si=_T4yD_ihGXFhokYS
#https://getbootstrap.com/docs/5.3/getting-started/introduction/
#https://www.geeksforgeeks.org/navigation-bars-in-flask/

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

#This function references the the HTML code in base.html.
@app.route('/')
def home():
    return render_template('base.html')


#Ensures that the web application is able to run
if __name__ == "__main__":
    app.run(debug=True) 


#How to push and pull changes to Git:
#cd poison-web
#git add .
#git commit -m ""
#git pull
#git push
