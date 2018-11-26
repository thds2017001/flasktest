# -*- coding: utf-8 -*-  
from app import app
from flask import render_template,session,redirect,url_for
from flask import request
import  hashlib
from .BaseCon import is_login




@app.route('/')
@is_login
def index():
	
	return render_template("index.html")




@app.route("/login",methods=['GET','POST'])
def login():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		app.logger.info('%s logged in successfully', username)
		#查询数据

		session['uid'] = 1
		return redirect("/")
	else:
		return render_template("login.html")
	