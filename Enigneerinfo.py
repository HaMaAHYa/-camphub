import requests as re
from bs4 import BeautifulSoup
import datetime


urlEni = 'https://www.camphub.in.th/engineer/'
urlCom = 'https://www.camphub.in.th/computer-it/'
urlArc = 'https://www.camphub.in.th/architect-finearts/'


eni_data = re.get(urlEni)
com_data = re.get(urlCom)
arc_data = re.get(urlArc)
eni_soup = BeautifulSoup(eni_data.text, 'html.parser')
com_soup = BeautifulSoup(com_data.text, 'html.parser')
arc_soup = BeautifulSoup(arc_data.text, 'html.parser')
find_eni = eni_soup.find_all('h2',{'class':'entry-title'})
find_com = com_soup.find_all('h2',{'class':'entry-title'})
find_arc = arc_soup.find_all('h2',{'class':'entry-title'})

print('*----------------------------*')
x = datetime.datetime.now()

print('ประจำวันที่',x)
print('\nค่ายวิศวะ')
for i in find_eni:
    i = str(i).split('"')
    x= str(i[-1]).split('</a></h2>')
    print('\n'+str(x[0])+'\n')

print('\nค่ายคอม')
for i in find_com:
    i = str(i).split('"')
    x= str(i[-1]).split('</a></h2>')
    print('\n'+str(x[0])+'\n')

print('\nค่ายถาปัต')
for i in find_arc:
    i = str(i).split('"')
    x= str(i[-1]).split('</a></h2>')
    print('\n'+str(x[0])+'\n')
print('*----------------------------*')
