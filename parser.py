#!/usr/bin/python3
from urllib import request
from bs4 import BeautifulSoup
from webpage import webpage
import re

class instaparse:
    def __init__(self, profile):
        self.profile = profile
        self.make_wordlist(self.profile.link)
        self.make_dictionary(self.profile.words)

    def make_wordlist(self, link):
        #getting captions
        response = request.urlopen(link)
        html = request.urlopen(link).read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        htmlstring = soup.body.script.contents[0]
        postbody = htmlstring.split("edge_media_to_caption")
        captions = []
        for i in range(1, len(postbody)):
            title = postbody[i].split("text\":")
            caption = title[1].split("}")
            captions.append(caption[0])
        #split into words
        for line in captions:
            captionwords = re.findall(r"\w+", line)
            for w in captionwords:
                self.profile.words.append(w)
    def make_dictionary(self, words):
        for w in words:
            self.profile.dic[w] += 1
