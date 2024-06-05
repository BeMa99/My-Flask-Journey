# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:24:39 2024

@author: BAyora
"""

from login import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=3000)