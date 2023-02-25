import os
from flask import Flask
app = Flask(_name_)

@app.rout("/")
  def hello():
    return "Hello World!"

@app.route('/how are you')
def hello():
    return 'I am good, how are you?'

if _name_ -- "_main_":
    app.run(host="0.0.0.0", port=8080)
