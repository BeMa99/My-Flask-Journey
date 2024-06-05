# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:09:47 2024

@author: BAyora
"""
#continuing login project with models. Moving all sql queries here from pages
#notice that parameter markers change when using mysql.connect, the '% s' becomes '%s'
from flask import current_app

def create_table():
    cursor = current_app.mysql.cursor()
    #Moving sql query from Workbench to models. No slanted quotes on user_created names
    cursor.execute("""
             CREATE TABLE IF NOT EXISTS users (
                 id INT(11) AUTO_INCREMENT PRIMARY KEY,
                 username VARCHAR(100) NOT NULL,
                 email VARCHAR(255) NOT NULL,
                 password VARCHAR(255) NOT NULL
                 )
             """)
    cursor.close()
    current_app.mysql.commit()
    
def drop_table():
    cursor = current_app.mysql.cursor()
    drop_query = "DROP TABLE IF EXISTS users"
    cursor.execute(drop_query)
    cursor.close()
    current_app.mysql.commit()
    
def register_user(username, email, password):
    cursor = current_app.mysql.cursor()
    insert_query = "INSERT INTO users VALUES(NULL, %s, %s, %s)"
    cursor.execute(insert_query, (username, email, password))
    cursor.close()
    current_app.mysql.commit()
    
def login_user(username, password):
    cursor = current_app.mysql.cursor()
    login_query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(login_query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

def check_user(username):
    cursor = current_app.mysql.cursor()
    check_user_query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(check_user_query, (username, ))
    user = cursor.fetchone()
    cursor.close()
    return user

def update_user(username, email, password, user_id):
    cursor = current_app.mysql.cursor()
    update_query = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s"
    cursor.execute(update_query, (username, email, password, user_id))
    cursor.close()
    current_app.mysql.commit()
    
def get_user(user_id):
    cursor = current_app.mysql.cursor()
    get_user_query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(get_user_query, (user_id, ))
    user = cursor.fetchone()
    cursor.close()
    return user