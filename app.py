from flask import Flask, render_template
import convert_google as cg
from catch_exchange import periods
import json

app = Flask(__name__)

@app.route('/')
def chart_tutorial():

    lperiods = periods()
    period = {}

    for p in lperiods:
        period[p] = cg.convert_to_DataTable(p)

    tempdata = json.dumps({'period':period, 'continent':cg.continents()})
    
    return render_template('chart_tutorial.html', tempdata=tempdata)