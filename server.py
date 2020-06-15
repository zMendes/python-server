import os
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/')
def control():
   return render_template('index.html')

@app.route('/status', methods = ['POST', 'GET'])
def status():
   global led, but, id, ts, pot
   if request.method == 'POST':
      print("Entei no post: {0}".format(request.form['TS']))
      status = request.form
      led = status['LED']
      id = status['ID']
      but = status['BUT']
      ts = status['TS'][0:19]
      pot = status['POT'][0:4]
      #return render_template("status.html", status = status)
   return jsonify({'led' : led,'but':but,"id":id,"ts":ts, "pot":pot}),200

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True,port=80)
