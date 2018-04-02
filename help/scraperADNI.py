#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:13:38 2018

@author: neurolab
"""

import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import re

class ScraperADNI():
    def __init__(self):
        # SETUP
        self.url_base_download = "https://utilities.loni.usc.edu/download/study?type=GET_FILES"
        url_login = "http://adni.loni.usc.edu/data-samples/access-data/"
        self.username = ""
        self.password = ""
        self.br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        self.br.set_handle_robots(False)
        self.br.set_handle_equiv(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_redirect(True)
        self.br.set_cookiejar(cj)
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) 
        
        # User Agent
        k = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
        
        # Add User Agent In Header
        self.br.addheaders = [('User-agent', k)]
        self.br.open(url_login)
         
        # Now Login Page Is Ready 
        try:
            self.br._factory.is_html = True
        except Exception as e:
            print e
        
        # Select Form By Index
        self.br.select_form(nr = 1)
        self.br.form['userEmail'] = self.username
        self.br.form['userPassword'] = self.password
        self.br.submit()
        
        x = self.br.find_link("Study Data")
        self.br.follow_link(x)
    
    def getDataList(self, link_item):        
        self.br.open(link_item)
        self.html = self.br.response().read()
        soup = BeautifulSoup(self.html)
        datasets = soup.findAll('td', {'class' : 'contentFont', 'width' : '540'})
        data_dict = {}
        for x in datasets:
            dataset_link = re.findall("downloadDataItem\(\'(.+?)\'\)\;", str(x.find('a')["onclick"]))[0]
            dataset_name = (x.text).replace("&#039;", "'")
            data_dict[dataset_name] = dataset_link
        
        return data_dict
            
    def getData(self, fileId, fileName):
        if self.html != None:
            # Find authKey and userId so mechanize can download files
            authKey = re.findall('authKey\=(.+?)"', self.html)[0]
            userId = re.findall('userId\=(.+?)"', self.html)[0]
        
            url_download = self.url_base_download
            url_download += "&userId=" + userId
            url_download += "&authKey=" + authKey
            url_download += "&fileId=" + fileId
            
            fileName = self.editFileName(fileName)
            
            return self.br.retrieve(url_download, fileName + '.csv')[0]
    
    def editFileName(self, fileName):
        fileName = fileName.replace(" ", "")
        
        return fileName
    
    def close(self):
        self.br.close()
        
