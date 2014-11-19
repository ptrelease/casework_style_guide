from __init__ import app
from flask import render_template
import os


@app.route('/')
def index():
  return render_template("index.html")

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5010)))

