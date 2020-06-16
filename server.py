import os
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/')
def control():
   return render_template('index.html')

@app.route('/home/status', methods = ['POST', 'GET'])
def status():
   global but, id, ts, pot
   if request.method == 'POST':
      print("Entei no post: {0}".format(request.form['TS']))
      status = request.form
      id = status['ID']
      but = status['BUT']
      ts = status['TS'][0:22]
      pot = status['POT'][0:4]
      #return render_template("status.html", status = status)
   return jsonify({"id":id,"ts":ts,"but":but, "pot":pot}),200

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True,port=80)
