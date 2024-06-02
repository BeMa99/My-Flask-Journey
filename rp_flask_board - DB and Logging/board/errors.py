# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:34:45 2024

@author: Berclay
"""

from flask import render_template, current_app, request#to add the url that the browser entered into your log.

def page_not_found(e):
    current_app.logger.info(f"'{e.name}' error ({e.code}) at {request.url}")
    return render_template("errors/404.html"), 404