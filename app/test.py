# -*- coding: utf-8 -*-  
from app import app
from flask import render_template,session,redirect,url_for
from flask import request
import  hashlib
from .BaseCon import is_login




@app.route('/test')
@is_login
def test():
	app.logger.info('这是我的测试')
	return "hah"


@app.route('/test1')
@is_login
def test1():
	app.logger.info('测试1')
	return "这是测试1"
	