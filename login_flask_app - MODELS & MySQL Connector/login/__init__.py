# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:34:32 2024

@author: Berclay
"""

from flask import Flask
#from flask_mysqldb import MySQL
import mysql.connector #using mysql connector
from .config import Config
from .models import create_table
from dotenv import load_dotenv

load_dotenv()

#mysql = MySQL()#assigning flask_mysql class to object

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.config.from_object(Config)
    #mysql.init_app(app)#initializing using flask_mysql
    app.mysql = mysql.connector.connect(
        host = app.config['MYSQL_HOST'],
        user = app.config['MYSQL_USER'],
        database = app.config['MYSQL_DB'],
        password = app.config['MYSQL_PASSWORD']
        )
    #create table from app run
    with app.app_context():
        create_table()
        
    
    from login import pages#placed after init to avoid circular imports
    #register blueprints
    app.register_blueprint(pages.bp)
    
    return app