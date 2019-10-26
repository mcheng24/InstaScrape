#!/usr/bin/python3

from collections import defaultdict
from bs4 import BeautifulSoup

class webpage:
    __init__(self, page):
        #original link
        self.link = ""
        #raw text
        self.raw = BeautifulSoup(html, 'html.parser').get_text()
        #instagram user
        self.user = ""
        #list of individual picture links
        self.links = []
        #list of all the words each post description
        self.words = []
        #dictionary of words and frequency
        self.dic = defaultdict(int)

    def tostring(self):
        print("User:  \"{}\"".format(self.user))
        print("Number of Pictures:  \"{}\"".format(len(self.links)))
        if len(self.dictionary) != 0:
	    f = open("Instapage.dict", "w+")
	    for w in sorted(self.dic, key=self.dic.get, reverse=True):
    	    	f.write(w + "\t" + str(self.dic[w]) + "\n")
	    f.close()
	else:
	    print("dictionary has no entries.")
