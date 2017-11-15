# -*- coding: utf-8 -*
import os
import sys
import urllib.request    # python 3
    
client_id = "KfLuH4yR9fhXz53BucJS"
client_secret = "WsRFgcYH1p"
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

encText = urllib.parse.quote("이름을 말하세요.")
data = "speaker=mijin&speed=0&text=" + encText;

response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('/home/pi/webapp/Speaker_mp3/start.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)

os.system("omxplayer -o local /home/pi/webapp/Speaker_mp3/start.mp3")


