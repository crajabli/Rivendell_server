from application import app
from flask import render_template, request, redirect, url_for, flash, session

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



@app.route('/logout')
def logout():
    return render_template('register.html')