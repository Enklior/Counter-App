from flask import Flask, render_template
from replit import db

app = Flask(__name__)

if 'number' not in db:
  db['number'] = 0

# root -> '/'
# increment -> '/increment'

# db -> {'number': 0}

### HTML & CSS ### Static


@app.route('/')
def home():
  # return show(page=home_page, number=db['number'])
  return render_template('index.html', number=db['number'])

@app.route('/increment')
def increment():
  # increments a number
  db['number'] += 1
  # print(db['number'])
  return render_template('index.html', number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  return render_template('index.html', number=db['number'])

app.run(host='0.0.0.0', port=81)