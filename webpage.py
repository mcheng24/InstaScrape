#!/usr/bin/python3

from collections import defaultdict
from bs4 import BeautifulSoup

class webpage:
    def __init__(self, page):
        self.user = page.split('/')[-2]
        #original link
        self.link = page
        #list of all the words each post description
        self.words = []
        #dictionary of words and frequency
        self.dic = defaultdict(int)

    def tostring(self):
        print("User:  \"{}\"".format(self.user))
        print("Number of words: \"{}\"".format(len(self.words)))
        if len(self.dic) != 0:
            f = open("Instapage.dict", "w+")
            for w in sorted(self.dic, key=self.dic.get, reverse=True):
    	        f.write(w + "\t" + str(self.dic[w]) + "\n")
	    #f.close()
        else:
            print("dictionary has no entries.")
