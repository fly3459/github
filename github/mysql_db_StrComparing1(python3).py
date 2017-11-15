# -*- coding: utf-8 -*
import pymysql

db=pymysql.connect(host="localhost",user="root",passwd="dkssud77",db="test", charset='utf8')

while (1):
          test=input("비교할 문자열을 입력하세요:")
          print (test)
          
          execute = "select str2 from speaker where str1='"+test+"'"

          cur  =db.cursor()
          try:
                cur.execute(execute)
                rs =cur.fetchone()
                
                print (rs[0])
                if rs[0]==test :
                 print ("성공")
                else :
                 print ("fail")

          except:
                print ("데이터베이스에 없는 내용입니다")


          cur.close()
          db.close()
