# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:34:32 2024

@author: Berclay
"""

from flask import Flask
from login import pages

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(pages.bp)
    return app