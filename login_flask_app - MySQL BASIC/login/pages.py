# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:00:20 2024

@author: Berclay
"""

from flask import Blueprint, render_template, request, session, redirect, url_for
import re
from login import mysql

bp = Blueprint("pages", __name__)

@bp.route("/")
@bp.route("/login", methods=('GET', 'POST'))
def login(app):
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = "Logged in successfully"
            return render_template('home.html', msg = msg)
        else:
            msg = "Incorrect Username/ Password!"
    return render_template('pages/login.html', msg = msg)

@bp.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@bp.route("/register", methods=('GET', 'POST'))
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not username.isalnum:
            msg = "Username must only contain characters and numbers"
        elif not username or not password or not email:
            msg = "Please fill out the form"
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = "You have registered successfully! "
            return render_template('pages/home.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form! '
    return render_template("pages/register.html", msg = msg)