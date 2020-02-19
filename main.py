from flask import Flask, render_template
import ream.convert

app = Flask(__name__)

@app.route('/')
def main():
    ream_dict = ream.convert.convert("test1.md", "test1.json")
    return render_template('h1.jinja2', ream_dict=ream_dict)

