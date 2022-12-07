import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()
#metin1 ve metin2 diye gir.
  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    kontrolhttp = "https://"
    kontrolhttps = "https://"
    metin1 = siteURL[:7]
    metin2 = siteURL[:8]
    if metin1 == "http://" or metin2 == "https://":
      print("Geçerli adres")
      dataOpen.write(siteURL+"\n")
    else:
      print("http:// ön ekini kullanarak geçerli bir adres giriniz ")
    dataOpen.close()

  def dataRead(self):
    dataOpen = open(self.dataFile, 'r')
    if os.stat(self.dataFile).st_size == 0:
      print("Henüz kaydedilmiş adres yok!")
    else:
      for dataShow in dataOpen:
        print(dataShow)
    dataOpen.close()