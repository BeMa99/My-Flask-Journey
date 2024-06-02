# -*- coding: utf-8 -*-
"""
Created on Fri May 31 06:11:01 2024

@author: Berclay
"""

from flask import Blueprint, render_template, redirect, request, url_for
from board.database import get_db

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]
        
        if message:
            db = get_db()
            db.execute("INSERT INTO post (author, message) VALUES (?, ?)", (author, message),)
            db.commit()
            return redirect(url_for("posts.posts"))
    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    #posts = []
    db = get_db()#connect to the database
    posts = db.execute("SELECT author, message, created FROM post ORDER BY created DESC").fetchall()
    return render_template("posts/posts.html", posts=posts)
