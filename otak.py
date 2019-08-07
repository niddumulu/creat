from urutkan import *

my_file = open("open.txt", "r")
kata = my_file.readlines()
PSN = (len(kata))
my_file.close()

my_file = open("hargasekarang.txt", "r")
hnow = my_file.read()
my_file.close()

hanow = float(hnow)
henow = float(1/hanow)

if PSN == 0:
   print ("open yuk")
   file_nama = open("open.txt", "r+")
   teks = file_nama.readlines()
   nama = hanow
   teks = format(nama)+"\n"
   file_nama.write(teks)
   file_nama.close()
   
   opena = 1
   teks = format(opena)
   file_nama = open("ekse.txt","w")
   file_nama.write(teks)
   file_nama.close()
   
   from gabungsteem import *

if PSN > 0:
 print ("siap")

 par5 = float(1.2/100)
 par4 = float(0.7/100)
 par3 = float(0.6/100)
 parmin =float((-2)/100)

 bar1 = float(kata[0])
 sbdb = round(1/bar1,3)
 print ("1 steem get  :",sbdb,"SBD")
 sbds = round(1/hanow,3)
 print ("kurs sekarang :",sbds,"SBD")

 up5 = 1/((1/bar1)-((1/bar1)*par5))
 up4 = 1/((1/bar1)-((1/bar1)*par4))
 up3 = 1/((1/bar1)-((1/bar1)*par3))

 parminn = 1/((1/bar1)-((1/bar1)*parmin))
 parmin7 = round(parminn,3)

 penandaharga = ((1/bar1)-(1/hanow))
 pndhrga = round(penandaharga,3)

 untung = round(1/up5,3)
 print (untung)

 if pndhrga > 0:
    print ("sudah untung :",pndhrga,"SDB")
   
    if hanow >= up3:
       #print ("up 3%")
       #print (hanow,up4)
      
       if hanow < up4:
          print ("belanja sbd")
         
          file_nama = open("open.txt", "r+")
          teks = file_nama.readlines()
          nama = hanow
          teks = format(nama)+"\n"
          file_nama.write(teks)
          file_nama.close()
         
          opena = 1
          teks = format(opena)
          file_nama = open("ekse.txt","w")
          file_nama.write(teks)
          file_nama.close()
         
          from gabungsteem import *
         
       if hanow >= up5:
          print ("untung 5%, jual sbd",untung)
          teks = format(untung)
          file_nama = open("ekse.txt","w")
          file_nama.write(teks)
          file_nama.close()
      
          from gabung import *
          from hapusbaris import *
         
 if pndhrga < 0:
    print ("mines :",pndhrga,"SDB")
   
    if hanow <= parmin7:
       #print (parmin7,bar1)
       print ("rugi 7%, ambil bawah belanja sbd")
      
       file_nama = open("open.txt", "r+")
       teks = file_nama.readlines()
       nama = hanow
       teks = format(nama)+"\n"
       file_nama.write(teks)
       file_nama.close()
      
       opena = 1
       teks = format(opena)
       file_nama = open("ekse.txt","w")
       file_nama.write(teks)
       file_nama.close()
      
       from gabungsteem import *
