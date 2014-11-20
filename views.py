from flask import render_template
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/platforms')
def platforms():
    return render_template("platforms.html")

@app.route('/whatwethinktheuserswant')
def what_we_think_the_users_want():
    return render_template("what_we_think_the_users_want.html")

@app.route('/usertypes')
def user_types():
    return render_template("user_types.html")




if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5010)))

