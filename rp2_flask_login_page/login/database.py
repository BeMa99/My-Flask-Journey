# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:58:03 2024

@author: Berclay
"""

from flask_mysqldb import MySQL

def get_sql(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Berclay@#99Man'
    app.config['MYSQL_DB'] = 'logindb'
    
    mysql = MySQL(app)
    return mysql