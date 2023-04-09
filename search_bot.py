'''
bu sayfa ile google da arama yapıp çıkan web siteleri arasında birini seçip içindeki data alınabiliyordu
donanım haber de bu linkdeki : https://www.donanimhaber.com/en-populer-programlama-dilleri-belli-oldu-zirve-yine-degismedi--159110

içeriği çok demiz alıp export edebiliyordum. Ancak google rechapcha ya takılıyorum 429 hatası veriyor.

'''
from bs4 import BeautifulSoup
from googlesearch  import search
import requests
query = "google"
url_list=[]

for url in search(query, num_results=1):
       url_list.append(url)
       print(url_list)


try:
    for item in url_list:
        if "donanimhaber" in item:
           # print("İstenilen değer: ", item)
            break
except Exception:
    print('url list patladı',Exception())



my_tag = 'section'
my_attrs = {'class': 'kolon yazi'}
my_text=my_tag,my_attrs

page = requests.get(item)
soup = BeautifulSoup(page.content, 'html.parser')
text=soup.findAll(my_text)[1]   ## ilgili div alındı

 # parse html content

for data in text(['style', 'script','span','aside','div']):   # gereksiz yerleri silip blog içindeki gerekli yazıyı alıyor.
        # Remove tags
        data.decompose()
       #print(text)   # hala içinde <li> gibi tagler var

lis = text.find_all(['li','figcaption','p','h2'])     #burada yukarıda gereksiz taglerden temizlenendikten sonra gerekli dataları kendi etiketlerinden çıkartıyor.
for li in lis:
    print(li.text) #artık bu data gönderilebilir.