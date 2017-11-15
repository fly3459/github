import MySQLdb
from flask import Flask
from flask import render_template
from flask import request
import Adafruit_DHT
import time #delay
import datetime #time pasing

app = Flask(__name__)



sensor = Adafruit_DHT.DHT11
pin = 2 #GPIO

def shutdown_server():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  func()


while True:
    @app.route('/shutdown')
    def shutdown(): #callback method
        shutdown_server()
        return 'Server shutting down...'

    @app.route('/')
    def mainpage():
        db = MySQLdb.connect("localhost", "root", "1234", "test")
        cur = db.cursor()
        cur.execute("select * from dhttest")
        row = cur.fetchall()

        templateData = {'data' : row}
        return render_template('DHT11_test_all.html',**templateData)

        cur.close()
        db.close()

    @app.route('/<year>/<month>/<day>/<hour>/<min>')
    def all(year,month,day,hour,min):
        db = MySQLdb.connect("localhost", "root", "1234", "test")
        cur = db.cursor()
        cur.execute("select * from dhttest where Year = %s and Month=%s and Day=%s and Hour=%s and Min=%s"%(year,month,day,hour,min))
        row = cur.fetchall()

        templateData = {'data' : row}
        return render_template('DHT11_test_all.html',**templateData)

        cur.close()
        db.close()

    if __name__ == "__main__":
      app.run(host='0.0.0.0', port=8888, debug=True)

    
