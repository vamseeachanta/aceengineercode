# -*- coding: utf-8 -*-
"""
Vamsee Achanta
Flask Project 1
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World. This is Vamsee's First Project!"
  
if __name__ == "__main__":
  app.run()