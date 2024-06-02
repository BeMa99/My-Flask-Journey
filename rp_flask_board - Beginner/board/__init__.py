# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:53:42 2024

@author: Berclay
"""

from flask import Flask
from board import pages

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    return app