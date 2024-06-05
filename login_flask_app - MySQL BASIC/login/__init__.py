# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:34:32 2024

@author: Berclay
"""

from flask import Flask
from flask_mysqldb import MySQL
from .config import Config

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from login import pages#placed after init to avoid circular imports
    app.register_blueprint(pages.bp)
    
    return app