import os
import time
from config import *

seconds= float(0)
minutes= int(-1)
hours= int(0)

#aiditele = input("Id telegram or group sasaran: ")
run = "dia"
while run.lower()=="dia":
  if seconds > 540:
      seconds = 0
      minutes = minutes+1      
      baris = minutes
      my_file = open("data.txt", "r")
      puisi = my_file.readlines()
      dataok = (puisi[baris])
      print (dataok)
      my_file.close()
      client.send_message('dogetipbotgroup', dataok)
      
      #print ('Pesan terkirim')
  if minutes > 450 :
     minutes = -1
     hours = hours+1
     
  #os.system('clear')
  seconds = (seconds+1)
  #print (hours," : ",minutes," : ", seconds)
  print ("menunggu ",seconds)
  time.sleep(1)
