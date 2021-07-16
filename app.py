from flask import Flask, render_template
from catch_exchange import read_data
import json

app = Flask(__name__)

@app.route('/')
def chart_tutorial():
    data = read_data("dataTable.json")

    tempdata = json.dumps({'title':'Currency Variation', 'data':data})

    return render_template('chart_tutorial.html', tempdata=tempdata)