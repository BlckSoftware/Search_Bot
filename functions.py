# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:19:59 2023

@author: hkarayazim
"""
'''google api key  :  AIzaSyA_NpKkRxxC4vshEmYsB7uEFjMu7JTaGEQ   

Bir API anahtarınız olduktan sonra, uygulamanız tüm sorgu URL'lerine key=yourAPIKey sorgu parametresini ekleyebilir. API anahtarı, URL'lere yerleştirmek için güvenlidir. Herhangi bir kodlamaya gerek yoktur.
'''

"""
BU DOSYA FONKSİYONLARIMIN BULUNDUĞU DOSYADIR.

Bu dosyanın kullanımı

1. adım import functions komutu ile bu dosya çağrılır
2. adım hangi fonksiyon çağrılacaksa functions.o fonksiyonun adı(istenilen  parametreler)
örnek : tag_result=functions.find_tag(url,tag)

search_word_in_url fonksiyonu verilen url deki belirtilen kelimeyi arar.

find_tag fonsyionu verilen url deki belirtilen html tag'ını arar

scrape_data fonsiyonu kap sitesindeki borsa istanbul da işlem gören şirketlerin kodlarını çekerek
örnekleme yaptım, fonsiyonun kullanımında 'text' diye belirttiğimiz değişken aslında 2 adet değerin
birlikte yazılması ile oluşuyor kullanırken aşağıdaki gibi kullanmamız gerekiyor

my_tag = 'div'
my_attrs = {'class': 'comp-cell _04 vtable'}
my_text=my_tag,my_attrs
print(functions.scrape_data(url,my_text))

burdaki my_tag ve my_attrs değişkenleri sitenin kaynak kodundaki şirket kodlarının bulunduğu div.

Bu örneği şu siteden aldım :https://medium.com/bili%C5%9Fim-hareketi/python-beautifulsoup-k%C3%BCt%C3%BCphanesi-ile-veri-kaz%C4%B1ma-e8076c7212a9

url="https://huseyinkarayazim.com.tr/api.php"
get_URL="https://huseyinkarayazim.com.tr/api.php?action=111222"
"""

import requests
import chardet
import re
import pandas as pd
#import openpyxl
import os
import time
#import pdfplumber
#import fitz
from bs4 import BeautifulSoup
#from transformers import pipeline

def welcome_screen(app_name,delay_time):
    os.system("cls" if os.name == "nt" else "clear")

    # Define the variables
    
    created_by = "Created by: Hüseyin Karayazım"
    github_link = "https://github.com/BlckSoftware"

    # Print the ASCII art with blue color
    print("\033[1;34m")
    print('''  
          
			 _________________________________________________
            /                                                 |
           |                                                  |
           |    _________________________________________     |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'

''')
    print(f"{app_name:^50}")
    print(f"{created_by:^50}")
    print(f"{github_link:^50}")
    print("\033[0m")
    time.sleep(delay_time)
    
    
    
def postAPI(url,payload):
    response=requests.post(url,payload)
    print("\nSTATUS : ",response.status_code)
    print("\n",response.json()['list'])

def getAPI(url):
    response=requests.get(url)
    print("\nSTATUS : ",response.status_code)
    print("\n",response.json()['list'])

def getAPIWiki(url):
    response=requests.get(url)
    print("\nSTATUS : ",response.status_code)
    print("\n",response.json())

    
def search_word_in_url(url, search_word):   
    
    r = requests.get(url)
    r.encoding = chardet.detect(r.content)['encoding']
    soup = BeautifulSoup(r.content, "html.parser")
    search_result = soup.find(text=lambda text: text and search_word in text)
    return search_result
    
    
    
def find_tag(url,tag):
     r = requests.get(url)
     r.encoding = chardet.detect(r.content)['encoding']
     soup = BeautifulSoup(r.content, "html.parser")
     p_tags = soup.find_all(tag)
     print(p_tags)  



     
def scrape_data(url,text):
   
 page = requests.get(url)
 soup = BeautifulSoup(page.content, 'html.parser')
 results = soup.findAll(text)
 results = str(results)
 results = results.replace(',', '')
 words = re.findall(r'>\S+</a>',results)
 list1=[]
 for i in words:
  i = i.replace('>','')
  i = i.replace('</a','')
  i = i.split(',')
  if len(i)>1:
   for x in range(len(i)):
    list1.append(i[x])
  else:
    list1.append(i[0])
 return list1

def export_data(text, e_type):
   
    # Export dosya tipine göre veriyi dışa aktarma işlemi
    if e_type.upper() == 'CSV':
        exported_data = text.to_csv(index=False)
        file_ext = "csv"
    elif e_type.upper() == 'EXCEL':
        exported_data = text.to_excel(index=False)
        file_ext = "xlsx"
    elif e_type.upper() == 'HTML':
        exported_data = text.to_html()
        file_ext = "html"
    elif e_type.upper() == 'JSON':
        exported_data = text.to_json()
        file_ext = "json"
   
    else:
        print("\nGeçersiz dosya tipi girdiniz!\n")
        return
  
    # Dışa aktarılan veriyi dosyaya kaydetme işlemi
    try:
        with open(f'exported_data.{file_ext}', 'x') as f:
            f.write(exported_data)
            print(f"{file_ext} dosyası başarıyla kaydedildi!\n")
    except FileExistsError:
        count = 1
        while True:
            file_name = f'exported_data_{count}.{file_ext}'
            if not os.path.isfile(file_name):
                break
            count += 1
        choice = input(f"\n{file_ext} dosyası zaten var, yeni dosya adı '{file_name}' olarak kaydedilsin mi? (e/h)")
        if choice.upper() == "E":
            with open(file_name, 'x') as f:
                f.write(exported_data)
                print(f"\n{file_ext} dosyası başarıyla kaydedildi!")
        else:
            print(f"\n{file_ext} dosyası kaydedilmedi.")
            
            
    '''        
            
def read_pdf(filename):
    with fitz.open(filename) as doc:
        text = ""
        for page in doc:
            text += page.get_text("text")
        return text                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                            
def question_answering(file_path):
 nlp = pipeline("question-answering")

 try:
    result = nlp(question="EDEBİYATIN SANAT AKIMLARI ile İLİŞKİSİ", context=functions.read_pdf(file_path))
    print(result)
 except Exception as e:
    print("Bir hata oluştu:", e)

 print(result)
                                                                                                                                                                                                                                             
            '''                                                                                                                                                                                                                                   
                                                                                    