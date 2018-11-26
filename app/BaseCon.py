# -*- coding: utf-8 -*-  
from flask import render_template,session,redirect,url_for

def is_login(funct):
	def inner(*args,**kwargs):
		uid = session.get('uid')
		if not uid:
			login_url=url_for('login')
			return redirect(login_url)
		return funct(*args,**kwargs)
	return inner


if __name__ == "__main__":
	pass
	#is_login()

	