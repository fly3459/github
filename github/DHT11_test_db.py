import MySQLdb
import Adafruit_DHT
import time #delay
import datetime #time pasing

sensor = Adafruit_DHT.DHT11
pin = 2 #GPIO

while True:
    wtime = datetime.datetime.now()
    t_year = wtime.strftime('%Y') # these are str type.
    t_month = wtime.strftime('%m')
    t_day = wtime.strftime('%d')
    t_hour = wtime.strftime('%H')
    t_min = wtime.strftime('%M')
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    print(t_year, t_month, t_day, t_hour, t_min, humidity, temperature)

    db = MySQLdb.connect("192.168.1.174","root","1234","test")
    cur = db.cursor()
    sql = "insert into dhttest values ('%s','%s','%s','%s','%s','%s','%s')" %(t_year, t_month, t_day, t_hour, t_min, humidity, temperature)

    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()

    cur.close()
    db.close()
    
    time.sleep(60)


    
