"""app"""
import json
from flask import Flask, render_template, request, jsonify
from ream.convert import ream2json

# instantiate the app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
#app.config.from_object(__name__)

# enable CORS
#CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/edit/<file_path>', methods=['POST', 'GET'])
def test_root(file_path):
    ream_dict = ream2json(file_path)
    file_name = file_path.split("/")[-1]
    print(ream_dict)
    return render_template('main.html', ream_dict=ream_dict, file_name=file_name)



@app.route('/oldedit/<file_path>', methods=['POST', 'GET'])
def main(file_path):
    ream_dict = ream2json(file_path)
    file_name = file_path.split("/")[-1]
    return render_template('edit/main.jinja2', ream_dict=ream_dict, file_name=file_name)



@app.route('/json/<file_path>')
def background_process(file_path):
    ream_dict = ream2json(file_path)
    return jsonify(ream_dict)


@app.route('/_test')
def test():
    a = request.args.get('a', 0, type=str)
    b = request.args.get('b', 0, type=str)
    c = request.args.get('c', 0, type=str)
    d = a+b+c
    print(d)
    with open("tt.txt", "w") as f:
        f.write(d)
    return jsonify(result=d)

if __name__ == '__main__':
    app.run()
