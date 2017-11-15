# -*- coding: utf-8 -*
import os
import sys
import urllib.request    # python 3 URL
import pymysql           # python 3 DB

client_id = "KfLuH4yR9fhXz53BucJS"
client_secret = "WsRFgcYH1p"
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)



#os.system("omxplayer -o local /home/pi/webapp/Speaker_mp3/start.mp3")

while(1):
    
    print("")
    Order = input("말씀하세요 : ")
    
    mydb=pymysql.connect(host="localhost",user="root",passwd="dkssud77",db="test", charset='utf8')
    query = "select num, str2 from speaker where str1='"+Order+"'"

    cur  = mydb.cursor()
    try:
        cur.execute(query)
        rs = cur.fetchone()
        print ("Sili : "+rs[1])
        
        index_db = str(rs[0])

        cur.close()
        mydb.close()
        os.system("omxplayer -o local /home/pi/webapp/Speaker_mp3/"+index_db+".mp3")
        
        
            
        

    except:
        print ("검색 실패")
        os.system("omxplayer -o local /home/pi/webapp/Speaker_mp3/error.mp3")

        Option_plus = input("추가하시겠습니까? : (Y / N)")

        if(Option_plus == "Y" or Option_plus == "y"):
            mydb()
            encText = urllib.parse.quote(rs[1])
            data = "speaker=mijin&speed=0&text=" + encText;
            response = urllib.request.urlopen(request, data=data.encode('utf-8'))
            rescode = response.getcode()
            if(rescode==200):
                response_body = response.read()
                with open("/home/pi/webapp/Speaker_mp3/"+index_db+".mp3", 'wb') as f:
                    f.write(response_body)
                
            else:
                print("Error Code:" + rescode)
        
            
        
        



