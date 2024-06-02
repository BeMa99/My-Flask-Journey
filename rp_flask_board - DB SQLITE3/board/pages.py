# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:10:39 2024

@author: Berclay
"""

from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/settings")
def settings():
    return "Hello Settings"