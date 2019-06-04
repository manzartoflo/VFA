#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:31:44 2019

@author: manzar
"""


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url = "https://www.vietfood.org.vn/en/members/members.html"
file = open('assignment.csv', 'w')
file.write("Company name, Address, Telephone, Fax, email\n")
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
links = soup.findAll('div', {'id': 'tab0'})
for link in links[0].ol:
    url_inside = urljoin(url, link.a.attrs['href'])
    #print(url_inside)
    req_inside = requests.get(url_inside)
    soup_inside = BeautifulSoup(req_inside.text, 'lxml')
    name = soup_inside.findAll('div', {'class': 'user-title'})[0].h3.text.replace('\n', '').replace(',', '')
    #print(name)
    about = soup_inside.findAll('div', {'class': 'user-description'})
    address = ''
    try:
        address = about[0].contents[0].split('Address :')[1].replace(',', '')
        tel = about[0].contents[2].split('Tel :')[1].replace(',', ' | ').replace('/', ' | ')
        fax = about[0].contents[4].split('Fax :')[1].replace(',', ' | ').replace('/', ' | ')
        email = about[0].contents[6].split('Email :')[1].replace(', ', ' | ')
        if(len(address) < 10):
            address = 'NaN'
    except:
        tel = about[0].contents[0].split('Tel :')[1].replace(',', ' | ').replace('/', ' | ')
        fax = about[0].contents[2].split('Fax :')[1].replace(',', ' | ').replace('/', ' | ')
        email = about[0].contents[4].split('Email :')[1].replace(', ', ' | ')
    
    if(len(tel) < 5):
            tel = 'NaN'
    if(len(fax) < 5):
            fax = 'NaN'
    if(len(email) < 5):
            email = 'NaN'
    if(len(address) < 10):
            address = 'NaN'
    
    file.write(name + "," + address + "," + tel + "," + fax + "," + email + "\n")
    print(tel.replace('\n', ''), fax.replace('\n', ''), email.replace('\n', ''))
file.close()























'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url = "http://www.vinafruit.com/vinafruit/member.php?lang=1"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
divs = soup.findAll('tr', {'bgcolor': '#FFFFFF'})
for div in divs:
    inside_soup = div.findAll('td')
    name = inside_soup[1].p.text.replace('\r', '').replace('\n', '').replace('\xa0', '')
    print(name)

'''