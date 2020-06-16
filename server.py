import os
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
global but0 = 0  
global id0= 0
global ts0 = "2020-01-01-00:00:00GMT" 
global pot0 = 0
global but1=0 
global id1 = 
global ts1 = "2020-01-01-00:00:00GMT" 
global pot1 = 0

app = Flask(__name__)
@app.route('/')
def control():
   return render_template('index.html')

@app.route('/home/status', methods = ['POST', 'GET'])
def status():

   if request.method == 'POST':
      print("Entei no post: {0}".format(request.form['TS']))
      if(request.form['ID']==0):
         status = request.form
         id0 = status['ID']
         but0 = status['BUT']
         ts0 = status['TS'][0:22]
         pot0 = status['POT'][0:4]
      else:
         id1 = status['ID']
         but1 = status['BUT']
         ts1 = status['TS'][0:22]
         pot1 = status['POT'][0:4]

   return jsonify({"id":id0,"ts":ts0,"but":but0, "pot":pot0},{"id":id1,"ts":ts1,"but":but1, "pot":pot1}),200

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True,port=80)
