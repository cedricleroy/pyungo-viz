import os
import sys
import glob

from flask import Flask, jsonify
from flask import render_template
from flask_cors import CORS

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DAGS = os.path.join(CURRENT_DIR, 'dags')
sys.path.append(DAGS)

modules = glob.glob(DAGS + '/*.py')
__all__ = [os.path.basename(f)[:-3] for f in modules
           if os.path.isfile(f) and not f.endswith('__init__.py')]


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return render_template('app.html')


@app.route("/data")
def load_data():
    from example import graph

    nodes = []

    for node in graph._nodes.values():
        nodes.append({
            'name': node._fct.__name__,
            'label': node._fct.__name__,
            'shape': 'rect',
        })

    for inp in graph.data.inputs:
        nodes.append({
            'name': inp,
            'label': inp,
            'shape': 'ellipse',
        })

    edges = []

    for node in graph._nodes.values():
        for inp in node.input_names:
            for node2 in graph._nodes.values():
                if inp in node2.output_names:
                    edges.append({
                        'from': node2._fct.__name__,
                        'to': node._fct.__name__,
                        'label': inp,
                    })
            if inp in graph.data.inputs:
                edges.append({
                    'from': inp,
                    'to': node._fct.__name__,
                    'label': inp,
                })

    return jsonify(
        {'nodes': nodes, 'edges': edges}
    )
