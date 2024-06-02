# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:53:42 2024

@author: Berclay
"""

import os #os is imported to load dotenv
from dotenv import load_dotenv #to load environment variables from the .env file 
from flask import Flask
from board import pages, posts, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env() #for variables that begin with flask
    
    database.init_app(app)
    
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using db: {app.config.get('DATABASE')}")
    return app