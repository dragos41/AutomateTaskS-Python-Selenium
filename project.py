from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import random
from collections import namedtuple
import time

TrackRec = namedtuple('TrackRec', [
    'title', 
    'artist',
    'timestamp'  
])
#chromedriver =r"C:\Users\Dan\Desktop\Sem 1 rezolvate\TSTS\Proiect2"
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://bandcamp.com/')

def Subpunct1():
  search_bar = browser.find_element_by_name('q')
  search_bar.send_keys("Lady Gaga",Keys.RETURN)
  
def Subpunct2():
  elements_of_search = browser.find_elements_by_class_name("result-info")
  print (len(elements_of_search))
  print ("Albume:")
  nr_in_lista = 0
  nr_albume = 0
  lista_indexi_albume = list()
  for option in elements_of_search:  
#    print (option.text)
    all_children_of_option = option.find_elements_by_css_selector("*")
#    print (( all_children_of_option[0].text))
    if (all_children_of_option[0].text =="ALBUM"):
      nr_albume += 1
      print ("{0}. {1}" .format(nr_albume,all_children_of_option[1].text))
      lista_indexi_albume.append(nr_in_lista)
    nr_in_lista += 1

#Se alege un album random din lista indexilor albumelor      
  print ("Album selectat: ")
  index_album_ales = random.choice(lista_indexi_albume)
  album_ales = elements_of_search[index_album_ales]
  print (album_ales.text)

#Apasare click pe albumul ales
  links =browser.find_elements_by_class_name("artcont")
  links[index_album_ales].click()

# Redare melodie din album
  tabel_cantece = browser.find_elements_by_class_name("play-col")
  song = random.choice(tabel_cantece)
  song.find_elements_by_css_selector("*")[0].click()
  
def is_playing():
  try:
    playbtn = browser.find_element_by_class_name('playbutton')
    return playbtn.get_attribute('class').find('playing') > -1
  except:
    return "EXCEPTIE"
  
def currently_playing():
  try:
    if is_playing():
        title = browser.find_element_by_class_name('title').text
        artist_detail = browser.find_element_by_css_selector('.detail-artist > a')
        artist = artist_detail.text
        return TrackRec(title, artist, time.ctime())

  except Exception as e:
    print('there was an error: {}'.format(e))

  return ' '
      
def convertTuple(tup): 
  str =  ''.join(tup) 
  return str
#    print("Value is: %s" % option.get_attribute("itemtype"))

Subpunct1()
Subpunct2()
i = 500

while i>0:
  fileHandle = open ( 'Log.txt',"r" )
  lineList = fileHandle.readlines()
  fileHandle.close()
  melodie = currently_playing()
  if  (melodie != ' ' ):
    if ( lineList[-1].find(melodie[0]) == -1):
      if ( lineList[-1].find(melodie[1]) == -1):
        with open("Log.txt", "a") as myfile:
          myfile.write(convertTuple(melodie) +'\n')
        print ("Adaugat ")
      
  i-=1

#browser.close()
