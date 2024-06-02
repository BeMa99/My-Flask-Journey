# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:08:33 2024

@author: Berclay
"""

import sqlite3
import click
from flask import current_app, g

def init_app(app):
    app.teardown_appcontext(close_db) #closing database connection when application context closes
    app.cli.add_command(init_db_command)
    
@click.command("init-db")
def init_db_command():
    db = get_db()
    
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))
        
    click.echo("You Successfully Initialized The Database!")
    
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
            )
        g.db.row_factory=sqlite3.Row
    
    return g.db

def close_db(e=None):#e for error - Flask design pattern for error handling
    db = g.pop("db", None)#g.pop is used to retrieve and remove the db connection object from the g object, if not present return 'None'
    if db is not None:
        db.close()