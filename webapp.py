#!/usr/bin/python
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/red', methods = ['POST'])	
def red():
	os.system("python /www/nightlight/static/color.py red")  
	return redirect('/')

@app.route('/yellow', methods = ['POST'])	
def yellow():
	os.system("python /www/nightlight/static/color.py yellow")  
	return redirect('/')

@app.route('/green', methods = ['POST'])	
def green():
	os.system("python /www/nightlight/static/color.py green")  
	return redirect('/')

@app.route('/blue', methods = ['POST'])	
def blue():
	os.system("python /www/nightlight/static/color.py blue")  
	return redirect('/')

@app.route('/clear', methods = ['POST'])	
def clear():
	os.system("python /www/nightlight/static/color.py clear")  
	return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
