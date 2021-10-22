from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return "Hello, rodrigao, do mano tonza!"
