#!/usr/bin/python3

from collections import defaultdict

class webpage:
    __init__(self, page):
        #original link
        self.link = ""
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
